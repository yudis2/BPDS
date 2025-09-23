# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis

1. Belum ada analisis performa karyawan untuk mengetahui KPI Employee
2. Tidak pedulinya HR untuk menilai kemampuan dan pengalaman karyawan membuat tingkat attrition tinggi.
3. Belum membuat laporan serta monitoring Performa Karyawan

### Cakupan Proyek

1. Explorasi Dataset JayaMaju dimana terdapat data karyawan untuk menilai performa dan tingkat attrition
2. Membuat Data Karyawan JayaMaju lebih exploratif untuk memprediksi tingkat attrition.
3. Visualisasi Dan Dashboard untuk memudahkan memonitoring data karyawan JayaMaju

### Persiapan

Sumber data: [JayaMaju Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

1. Buka terminal atau PowerShell.
2. Membuat virtual Environment
```
conda create --name jayamaju-segmentation python=3.9
```
3. Aktifkan virtual Environment
```
conda activate jayamaju-segmentation
```
4. Install semua library yang dibutuhkan
```
pip install -r requirements.txt
```



### 🛠️ Cara Menjalankan Aplikasi
1. Clone Repository
```
git clone https://github.com/yudis2/BPDS.git
cd BPDS
```
2. Run Dashboard Jaya Maju (Streamlit)
```
streamlit run prediction.py
```
3. Akses Dashboard Jaya Maju
```
http://localhost:(port)/
```
4. Akses Prediksi Karyawan
```
akses menu sidebar Prediction Employee
```

## Business Dashboard
[Dashboard JayaMaju](https://yudisdwi.streamlit.app/)
Human Resource Dashboard yang digunakan untuk melakukan prediksi kemungkinan karyawan resign (attrition prediction). Berikut penjelasannya:
Struktur Dashboard

Sidebar (kiri):
• Berisi menu navigasi dengan beberapa pilihan:

• Data Overview → untuk menampilkan ringkasan data karyawan.

• Visualization Data → untuk menampilkan visualisasi grafik/statistik data karyawan.

• Prediction Employee → menu aktif saat ini, digunakan untuk memprediksi kemungkinan karyawan resign.

• Result & Recommendation → menampilkan hasil analisis dan rekomendasi tindak lanjut.

## Conclusion

Dashboard ini dibuat untuk membantu HR dalam:

• Mengidentifikasi karyawan berisiko resign lebih awal.

• Mengambil tindakan pencegahan (misalnya memberi insentif, rotasi jabatan, pelatihan, atau perhatian khusus).

• Mendukung pengambilan keputusan berbasis data (data-driven HR)

Fitur-fitur seperti `Age`, `MonthlyIncome`, `OverTime`, dan `TotalWorkingYears` terbukti memiliki pengaruh besar dalam menentukan apakah seorang karyawan akan keluar dari perusahaan. 


### Rekomendasi Action Items (Optional)

Bedasarkan hasil analisis pada dashboard untuk probabilty karyawan yang melakukan resign, untuk dilakukan :
- Peningkatan Kompensasi & Benefit.
- Rotasi atau Penugasan Baru agar karyawan memiliki tantangan baru.
- Monitoring jam kerja dan berikan kesempatan agar memiliki kesempatan yang luas.
