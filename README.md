# Laporan Proyek Machine Learning
### Nama : Aditya Eka Purwanto
### Nim : 211351005
### Kelas : Malam B

## Domain Proyek

Asuransi kesehatan sangat penting karena memberikan akses ke perawatan medis yang terjangkau, melindungi individu dari beban keuangan yang besar, mendorong pencegahan dan pengobatan dini, serta meningkatkan kualitas hidup dan produktivitas.

## Business Understanding

Proyek estimasi harga asuransi kesehatan menjadi yang penting juga karena memberikan solusi untuk menentukan premi asuransi yang lebih adil, memungkinkan calon peserta asuransi membuat keputusan yang lebih baik, membantu perusahaan asuransi mengelola risiko, meningkatkan efisiensi operasional, dan memfasilitasi pengembangan produk asuransi yang inovatif.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Calon peserta yang tidak tau kisaran harga asuransi

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Diharapkan agar calon peserta asuransi memiliki estimasi berapa biaya yang harus mereka keluarkan untuk membayar asuransi tersebut dengan beberapa kriteria yang akan mereka input.


### Solution statements
- Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
- Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.
- Membuat sebuah sistem yang dapat melakukan estimasi harga premi asuransi kesehatan yang dapat diakses oleh calon peserta asuransi berbasis web
- Model yang dibuat menggunakan metode estimasi dengan algoritma regresi linear 

## Data Understanding
dataset yang digunakan diambil dari Kaggle milik [MIRI CHOI](https://www.kaggle.com/mirichoi0218) dataset tersebut berisi sekumpulan data biaya yang dibayarkan untuk asuransi kesehatan yang berisi umur, jenis kelamin, BMI, jumlah anak, wilayah peserta, perokok atau bukan dan biaya yang dibayarkan

[Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance/data)

### Variabel-variabel:
Age: usia penerima manfaat utama
Sex: jenis kelamin peserta asuransi, perempuan, laki-laki
BMI: Indeks massa tubuh, memberikan pemahaman tentang tubuh, berat badan yang relatif tinggi atau rendah terhadap tinggi badan,
indeks obyektif berat badan (kg/m^2) dengan menggunakan rasio tinggi dan berat badan, idealnya 18,5 sampai 24,9
Children: Jumlah anak yang ditanggung oleh asuransi kesehatan / Jumlah tanggungan
Smoker: Merokok
Region: wilayah tempat tinggal penerima manfaat di AS, timur laut, tenggara, barat daya, barat laut.
Charges: Biaya pengobatan perorangan yang ditagihkan oleh asuransi kesehatan

## Data Preparation
## Import Library
Library yang dibutuhkan dalam pembuatan model estimasi premi asuransi kesehatan yaitu:
``bash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
``

## Data Cleaning

Untuk melakukan sebuah proses menggunakan algoritma regresi linear maka tipe data yang dibutuhkan adalah integer. Terdapat 3 kolom dalam dataset yang memiliki tiper data object, maka dari itu perlu dilakukannya konversi tipe data menjadi integer menggunakan kode

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Deployment
[Hasil Deploy](https://estimasi-medical-adit.streamlit.app/).

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

