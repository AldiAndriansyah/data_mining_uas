import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Baca data
data_startup = pd.read_csv('50_Startups.csv', delimiter='\t')

# Identifikasi field yang memiliki data kosong (NaN)
fields_with_nan = data_startup.columns[data_startup.isna().any()].tolist()

# Isi data yang kosong menggunakan nilai mean
imputer = SimpleImputer(strategy='mean')
data_startup[fields_with_nan] = imputer.fit_transform(data_startup[fields_with_nan])

# Lakukan one-hot encoding ke field State
encoder = OneHotEncoder()
state_encoded = encoder.fit_transform(data_startup[['State']])

# Buat field baru yaitu Tax
data_startup['Tax'] = (data_startup['Profit'] + data_startup['Marketing Spend'] + data_startup['Administration']) * 0.05

# Jalankan StandardScaler untuk melakukan penskalaan fitur
scaler = StandardScaler()
data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']] = scaler.fit_transform(data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']])

# Tampilkan hasil pre-processing
print(data_startup.head())

# Simpan data hasil pre-processing ke dalam file CSV
data_startup.to_csv('preprocessed_startup_data.csv', index=False)
