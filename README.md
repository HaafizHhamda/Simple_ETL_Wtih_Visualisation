# Simple_ETL
## Problem Background

Di era pengambilan keputusan berbasis data, perusahaan sering kali memiliki data dalam jumlah besar namun belum dimanfaatkan secara optimal. Tanpa proses eksplorasi yang tepat, pola, tren, dan anomali dalam data sulit untuk diidentifikasi, sehingga keputusan bisnis berisiko kurang akurat. Oleh karena itu, Exploratory Data Analysis (EDA) diperlukan untuk memahami karakteristik data, mengevaluasi kualitas data, serta menggali insight awal sebelum digunakan untuk analisis lanjutan atau pengambilan keputusan strategis.

## Problem

Proyek ini bertujuan untuk melakukan Exploratory Data Analysis (EDA) pada sebuah dataset guna mengidentifikasi pola, tren, dan hubungan antar variabel. Hasil analisis diharapkan dapat menghasilkan insight yang relevan serta rekomendasi berbasis data untuk mendukung pengambilan keputusan yang lebih tepat dan efektif.

## Project Wisdom

Proyek ini menunjukkan bahwa Exploratory Data Analysis (EDA) adalah langkah krusial untuk memahami data sebelum pengambilan keputusan. Dengan data yang bersih, tervalidasi, dan diproses melalui pipeline otomatis, insight yang dihasilkan menjadi lebih akurat dan dapat dipercaya.

Lebih dari sekadar analisis teknis, proyek ini menegaskan bahwa nilai data muncul ketika hasil eksplorasi diterjemahkan menjadi rekomendasi bisnis yang relevan dan berdampak.

## Data

## Columns Description

- **order_id**: Unique identifier for each sales transaction.
- **date**: Date when the transaction occurred.
- **product**: Name of the product sold.
- **category**: Product category classification.
- **price**: Unit price of the product.
- **quantity**: Number of units purchased per transaction.
- **total_sales**: Total sales amount per transaction (price × quantity).
- **customer_name**: Identifier or name of the customer.
- **customer_location**: Geographic location of the customer.
- **payment_method**: Method of payment used in the transaction.
- **status**: Current status of the transaction (e.g., completed, cancelled).



## Method

- **Pengumpulan dan Penyimpanan Data**
Memilih dataset mentah dan menyimpannya di PostgreSQL (berbasis Docker) tanpa modifikasi apa pun.

- **Pembersihan dan Persiapan Data**
Mengekstrak data menggunakan Python, menghapus duplikat, menstandarkan nama kolom, dan menangani nilai yang hilang.
Dataset yang telah dibersihkan diekspor ke file CSV terstruktur.

- **Validasi Data**
Melakukan pemeriksaan kualitas data menggunakan Great Expectations untuk memastikan akurasi, konsistensi, dan keandalan data.

- **Otomatisasi Alur Kerja Data**
Membangun alur kerja data otomatis menggunakan Apache Airflow untuk mengoordinasikan proses ekstraksi, pembersihan, dan pemuatan data.

- **Pengkodean & Visualisasi Data**
Memuat data yang telah dibersihkan ke Elasticsearch dan mengembangkan dasbor Kibana interaktif untuk analisis data eksploratori.

- **Wawasan & Rekomendasi Bisnis**
Menghasilkan wawasan dari analisis data dan memberikan rekomendasi berbasis data yang selaras dengan tujuan bisnis yang telah ditetapkan.


## Tech Stack & Skills
- Python
- Apache Airflow: Workflow orchestration and pipeline automation.
- Great Expectations: Data quality validation and consistency checks.
- NoSQL Concepts: Understanding of NoSQL database architecture and use cases.
- Data Preparation: Data cleaning and transformation before ingestion into NoSQL databases.
- Kibana: Data exploration, visualization, and interactive dashboard creation.
- GitHub

## Reference

- Laporan analisis great expectation data berupa notebook 
- `P2M3_haafizhhamda_DAG.py` berupa hasil ETL
- Images merupakan hasil visualisasi analysis

---
