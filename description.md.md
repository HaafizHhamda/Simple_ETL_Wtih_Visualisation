# Judul Project
Sales Data Pipeline: Extract, Transform, Load, and Visualize

## Problem Background
Objective Project — Amazon Sales 2025

Proyek ini bertujuan untuk menganalisis pola penjualan di platform
Amazon guna mengidentifikasi faktor-faktor utama yang memengaruhi
performa bisnis. Fokus analisis mencakup: 1. Menggali hubungan antara
kategori produk, lokasi pelanggan, dan metode pembayaran terhadap total
penjualan. 2. Menemukan waktu dan strategi promosi paling efektif untuk
meningkatkan pendapatan. 3. Memberikan rekomendasi berbasis data bagi
tim sales, marketing, dan operasional agar strategi bisnis dapat
diarahkan pada produk dan segmen pelanggan paling menguntungkan.

Permasalahan utama yang ingin diselesaikan adalah memahami bagaimana pola penjualan dan perilaku pelanggan di platform Amazon dapat memberikan wawasan bagi strategi bisnis yang lebih efisien dan menguntungkan.
Proyek ini menyoroti kebutuhan untuk mengintegrasikan data dari berbagai sumber penjualan dan melakukan analisis  agar proses pengambilan keputusan menjadi lebih cepat dan akurat.


## Project Output
Output dari proyek ini berupa **dashboard interaktif dan laporan analisis data penjualan Amazon** yang menampilkan:
- Tren penjualan per kategori dan wilayah.
- Analisis metode pembayaran dan dampaknya terhadap total transaksi.
- Rekomendasi produk dan waktu promosi terbaik.
- Dataset bersih hasil pipeline ETL dengan validasi menggunakan Great Expectations.



## Data
Dataset yang digunakan berasal dari hasil pembersihan tahap ETL sebelumnya dengan nama **P2M3_haafizhhamda_data_clean.csv**.  
Dataset ini berisi **250 baris** dan **11 kolom**.

**Contoh kolom utama:** Order ID, Date, Product, Category, Price, Quantity...  
**Tipe data dalam dataset:** {dtype('O'): 8, dtype('int64'): 3}  
**Jumlah missing value:** 0

Dataset ini berisi kombinasi data numerik, kategorikal, dan teks yang telah dinormalisasi.  
Seluruh kolom telah melalui proses validasi dengan *Great Expectations* untuk memastikan konsistensi tipe data dan nilai.  

## Method
Metode utama yang digunakan adalah **ETL Batch Processing** dengan tahapan:
1. **Extract** – Mengambil data dari PostgreSQL.
2. **Transform** – Normalisasi kolom, konversi tipe data, dan penghapusan null.
3. **Load** – Menyimpan hasil ke data warehouse untuk analitik.
4. **Validate** – Menggunakan Great Expectations (`expect_column_values_to_not_be_null`, `expect_column_values_to_be_between`, dll).

Pipeline dijalankan secara **terjadwal (batch)** dengan **Airflow DAG** setiap malam hari.

## Stacks
- **Bahasa Pemrograman:** Python 3.10  
- **Database:** PostgreSQL  
- **Workflow Orchestration:** Apache Airflow  
- **Data Validation:** Great Expectations  
- **Libraries:** Pandas Airflow Operators  
- **Environment:** Docker Container

## Reference
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Great Expectations Docs](https://docs.greatexpectations.io/)
- [Pandas Library](https://pandas.pydata.org/)
- [Project Repository Example](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
