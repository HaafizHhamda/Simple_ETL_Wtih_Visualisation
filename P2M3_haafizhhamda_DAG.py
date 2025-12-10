from airflow import DAG
import pandas as pd
import datetime as dt
from datetime import timedelta
from elasticsearch import Elasticsearch, helpers

# Catatan: Pada Airflow 2.x, import yang direkomendasikan:
# from airflow.operators.bash import BashOperator
# from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
# untuk connect postgre dengan python
import psycopg2 as db


def extract_data():
    """
    Extract data dari PostgreSQL dan simpan sebagai CSV raw.

    Langkah:
    1) Membuat koneksi ke PostgreSQL via psycopg2.
    2) Menjalankan query SELECT * FROM table_m3.
    3) Menyimpan hasil query ke file CSV raw di folder dags.

    Output:
        /opt/airflow/dags/P2M3_haafizhhamda_data_raw.csv
    """
    # String koneksi ke Postgres di jaringan docker-compose (service name: postgres)
    conn_string = (
        "dbname='postgres' "
        "host='postgres' "
        "user='airflow' "
        "password='airflow' "
        "port = 5432"
    )

    # Buat koneksi ke database
    conn = db.connect(conn_string)

    # Eksekusi query dan muat ke DataFrame
    table_m3 = pd.read_sql("SELECT * FROM table_m3", conn)

    # Simpan hasil extract ke CSV raw (tanpa index)
    table_m3.to_csv('/opt/airflow/dags/P2M3_haafizhhamda_data_raw.csv', index=False)
    print("-------table_m3 Saved (RAW)------")

    # Tutup koneksi untuk menghindari kebocoran koneksi
    conn.close()


def transform():
    """
    Transformasi data mentah menjadi data bersih.

    Langkah:
    1) Membaca CSV raw.
    2) Normalisasi nama kolom (rename).
    3) Menghapus baris dengan missing values (dropna).
    4) Menghapus baris duplikat (drop_duplicates).
    5) Menyimpan hasil sebagai CSV clean.

    Output:
        /opt/airflow/dags/P2M3_haafizhhamda_data_clean.csv
    """
    # 1. Baca file csv (hasil extract)
    table_m3 = pd.read_csv('/opt/airflow/dags/P2M3_haafizhhamda_data_raw.csv')

    # 2. Ubah nama kolom (normalisasi) -> pastikan nama kolom sumber sesuai
    table_m3 = table_m3.rename(columns={
        'Order ID': 'order_id',
        'Date': 'date',
        'Product': 'product',
        'Category': 'category',
        'Price': 'price',
        'Quantity': 'quantity',
        'Total Sales': 'total_sales',
        'Customer Name': 'customer_name',
        'Customer Location': 'customer_location',
        'Payment Method': 'payment_method',
        'Status': 'status'
    })

    # 3. Hapus baris yang ada nilai kosong (missing values)
    #    Jika ingin lebih hati-hati, bisa spesifik kolom kritikal saja: dropna(subset=['order_id', ...])
    table_m3 = table_m3.dropna()

    # 4. Hapus baris yang duplikat berdasarkan seluruh kolom
    table_m3 = table_m3.drop_duplicates()

    # 5. Simpan hasilnya (tanpa index)
    table_m3.to_csv('/opt/airflow/dags/P2M3_haafizhhamda_data_clean.csv', index=False)
    print("Data cleaned & saved successfully!")


def load_data():
    """
    Load data bersih ke Elasticsearch (bulk indexing).

    Langkah:
    1) Membaca CSV clean.
    2) Membuat koneksi ke Elasticsearch (service name: elasticsearch).
    3) Melakukan bulk index ke index: sales_transaction (satu dokumen per baris).
    """
    # Baca data bersih yang sudah ditransformasi
    df = pd.read_csv('/opt/airflow/dags/P2M3_haafizhhamda_data_clean.csv')

    # Koneksi ke Elasticsearch (sesuaikan host/port dengan docker-compose)
    es = Elasticsearch("http://elasticsearch:9200")

    # Siapkan actions untuk bulk indexing
    actions = [
        {
            "_index": "sales_transaction",  # nama index tujuan
            "_id": i,                       # optional: gunakan i sebagai _id
            "_source": r.to_dict()          # body dokumen: dict dari baris DataFrame
        }
        for i, r in df.iterrows()
    ]

    # Eksekusi bulk
    response = helpers.bulk(es, actions)
    print(response)  # tuple (success_count, details)


# Default arguments DAG (owner, tanggal mulai, retry)
default_args = {
    'owner': 'apis',
    # start_date disesuaikan UTC; dikurangi 7 jam untuk WIB (Asia/Jakarta)
    'start_date': dt.datetime(2024, 11, 1) - dt.timedelta(hours=7),
    'retries': 1,                                 # jumlah percobaan ulang jika gagal
    'retry_delay': dt.timedelta(minutes=5),        # jeda retry
}

# Definisi DAG: jadwal, default args, dan no catchup untuk menghindari backlog run
with DAG(
    'milestone3',
    default_args=default_args,
    schedule_interval='10-30/10 9 * * 6',  # Menit 10,20,30 pada jam 09:00 setiap Sabtu
    catchup=False
) as dag:

    # Task dummy untuk log awal
    print_starting = BashOperator(
        task_id='starting',
        bash_command='echo "I am reading the CSV now....."'
    )

    # Task Extract dari PostgreSQL
    extractData = PythonOperator(
        task_id='extract_from_postgre',
        python_callable=extract_data
    )

    # Task Transform dengan Pandas
    transformData = PythonOperator(
        task_id='transform_data_by_python',
        python_callable=transform
    )

    # Task Load ke Elasticsearch
    loadData = PythonOperator(
        task_id='load_into_database',
        python_callable=load_data
    )

    # Task dummy untuk log akhir
    print_stop = BashOperator(
        task_id='stopping',
        bash_command='echo "I done converting the CSV"'
    )

# Urutan dependency antar task (starting -> extract -> transform -> load -> stop)
print_starting >> extractData >> transformData >> loadData >> print_stop
