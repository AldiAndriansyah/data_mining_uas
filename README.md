# Data dan Fungsi pada Perusahaan dan Karyawan

## Data
Data dalam skrip ini mencakup informasi tentang perusahaan dan karyawan. Berikut adalah rincian data yang tersedia:

### Perusahaan
Ada tiga perusahaan yang diidentifikasi dengan nama dan informasi domain mereka. Setiap perusahaan juga memiliki daftar klien dengan nama dan negara.

### Karyawan
Ada tiga karyawan yang diidentifikasi dengan nama lengkap, nama perusahaan, dan detail karyawan lainnya seperti ID karyawan dan nama perusahaan tempat mereka bekerja.

## Fungsi-fungsi
Berikut adalah fungsi-fungsi yang disediakan dalam skrip:

### 1. sort_companies()
Fungsi ini mengurutkan perusahaan berdasarkan domain dalam urutan menurun dan mengembalikan daftar perusahaan yang diurutkan dengan nama dan domain mereka.

### 2. print_company_domains()
Fungsi ini mencetak domain setiap perusahaan bersama dengan jumlah klien yang mereka miliki.

### 3. get_employees_with_domains()
Fungsi ini mengembalikan daftar karyawan beserta nama perusahaan dan domain perusahaan tempat mereka bekerja.

### 4. get_employees_by_company()
Fungsi ini mengembalikan daftar perusahaan dengan daftar karyawan yang bekerja di masing-masing perusahaan.

## Penggunaan
Anda dapat menggunakan fungsi-fungsi ini untuk menganalisis data perusahaan dan karyawan. Berikut adalah beberapa contoh penggunaan:

- `sort_companies()`: Mengurutkan perusahaan berdasarkan domain.
- `print_company_domains()`: Mencetak domain setiap perusahaan.
- `get_employees_with_domains()`: Mendapatkan daftar karyawan dengan nama perusahaan dan domain.
- `get_employees_by_company()`: Mendapatkan daftar perusahaan dengan daftar karyawan yang bekerja di masing-masing perusahaan.



# Preprocessing Data Start-up

## Deskripsi
Repositori ini berisi skrip Python untuk melakukan preprocessing data pada dataset start-up. Preprocessing ini mencakup identifikasi dan pengisian nilai-nilai kosong (NaN), one-hot encoding untuk kolom State, perhitungan kolom baru Tax, dan penskalaan fitur menggunakan StandardScaler.

## Cara Penggunaan
1. Pastikan Python dan semua library yang diperlukan telah terinstal di lingkungan Anda.
2. Unduh dataset "50_Startups.csv" dan simpan dalam folder yang sama dengan skrip Python.
3. Jalankan skrip `preprocess_startup_data.py` dengan perintah `python preprocess_startup_data.py`.
4. Hasil pre-processing akan ditampilkan di konsol dan disimpan dalam file CSV baru bernama `preprocessed_startup_data.csv`.

## Penjelasan Kode
- `import pandas as pd`: Mengimpor library pandas untuk manipulasi data.
- `from sklearn.preprocessing import OneHotEncoder, StandardScaler`: Mengimpor class OneHotEncoder dan StandardScaler dari library scikit-learn untuk preprocessing.
- `from sklearn.impute import SimpleImputer`: Mengimpor class SimpleImputer dari scikit-learn untuk mengisi nilai kosong.
- `data_startup = pd.read_csv('50_Startups.csv', delimiter='\t')`: Membaca dataset dari file CSV menggunakan pandas, dengan menggunakan tab sebagai delimiter.
- `fields_with_nan = data_startup.columns[data_startup.isna().any()].tolist()`: Mengidentifikasi kolom-kolom yang memiliki nilai kosong (NaN).
- `imputer = SimpleImputer(strategy='mean')`: Membuat objek imputer untuk mengisi nilai kosong dengan nilai rata-rata.
- `data_startup[fields_with_nan] = imputer.fit_transform(data_startup[fields_with_nan])`: Mengisi nilai kosong dengan nilai rata-rata menggunakan metode fit_transform dari imputer.
- `encoder = OneHotEncoder()`: Membuat objek encoder untuk melakukan one-hot encoding.
- `state_encoded = encoder.fit_transform(data_startup[['State']])`: Melakukan one-hot encoding pada kolom State.
- `data_startup['Tax'] = (data_startup['Profit'] + data_startup['Marketing Spend'] + data_startup['Administration']) * 0.05`: Membuat kolom baru Tax yang dihitung sebagai 5% dari total Profit, Marketing Spend, dan Administration.
- `scaler = StandardScaler()`: Membuat objek scaler untuk melakukan penskalaan fitur.
- `scaled_features = scaler.fit_transform(data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']])`: Melakukan penskalaan fitur menggunakan metode fit_transform dari scaler.
- `data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']] = scaled_features`: Menetapkan fitur yang telah di-skala kembali ke DataFrame.
- `data_startup.to_csv('preprocessed_startup_data.csv', index=False)`: Menyimpan hasil pre-processing ke dalam file CSV baru.

---

Anda dapat menyesuaikan penjelasan ini sesuai dengan kebutuhan Anda dan menambahkan informasi tambahan jika diperlukan.
