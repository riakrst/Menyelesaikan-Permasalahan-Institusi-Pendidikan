# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan berprestasi. Namun, salah satu tantangan utama yang sedang mereka hadapi adalah tingginya angka dropout atau mahasiswa yang tidak menyelesaikan pendidikannya.

Masalah ini tidak hanya mempengaruhi reputasi institusi, tetapi juga berpotensi berdampak pada kualitas lulusan serta pengelolaan sumber daya kampus secara keseluruhan. Oleh karena itu, Jaya Jaya Institut ingin menerapkan solusi berbasis data untuk memahami faktor-faktor yang berpengaruh terhadap dropout dan mengembangkan sistem yang mampu memantau serta memprediksi risiko dropout secara dini.

### Permasalahan Bisnis
- Tingginya angka mahasiswa dropout.
- Belum adanya sistem prediktif untuk mendeteksi potensi dropout secara dini.
  
### Cakupan Proyek
- Menganalisis performa mahasiswa berdasarkan data historis.
- Membuat dashboard analisis untuk memantau indikator kunci performa mahasiswa.
- Membangun model machine learning untuk memprediksi kemungkinan mahasiswa akan dropout.
- Mengembangkan prototipe aplikasi berbasis Streamlit yang siap digunakan.

### Persiapan

**Sumber data:** [Data students performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup environment:**
```
# Clone repository dari GitHub
git clone https://github.com/riakrst/Menyelesaikan-Permasalahan-Institusi-Pendidikan.git
cd Menyelesaikan-Permasalahan-Institusi-Pendidikan

# Membuat virtual environment
python -m venv venv

# Aktivasi environment
# Untuk pengguna Windows
venv\Scripts\activate

# Untuk pengguna macOS/Linux
source venv/bin/activate

# Install seluruh dependensi
pip install -r requirements.txt
```

## Business Dashboard
Untuk menjawab tantangan tingginya tingkat dropout di Jaya Jaya Institut, telah dibangun sebuah business dashboard menggunakan Metabase. Dashboard ini menyajikan ringkasan performa mahasiswa, visualisasi statistik akademik, serta analisis faktor-faktor utama yang berkontribusi terhadap dropout berdasarkan hasil feature importance dari model machine learning.
- **Email akses:** root@mail.com
- **Password akses:** root123
- **File Metabase DB:** metabase.db.mv.db (sudah disertakan dalam repositori)
- **URL Lokal:** http://localhost:3002
- **Screenshot:** folder riakrst-dashboard (terlampir)

### Insight Visualisasi:
- **Summary:**
![image](https://github.com/user-attachments/assets/3aa17c2c-dd97-46cc-846d-a46b90790878)

- **Tingkat Dropout Tinggi:** Dari total 4.424 mahasiswa, sebanyak 1.421 (32,1%) mengalami dropout, menunjukkan perlunya perhatian serius.
![image](https://github.com/user-attachments/assets/19d5e5f4-5738-4590-899a-f7a0aca3f565)

- **Beasiswa dan Pembayaran UKT:** Mayoritas mahasiswa dropout bukan penerima beasiswa (90,57%), dan 67,8% mahasiswa yang dropout memiliki status pembayaran UKT yang lunas.
![image](https://github.com/user-attachments/assets/f830de92-b57d-4076-aef4-1286ed6bf180)

- **Gender & Waktu Kuliah:** Proporsi dropout antara laki-laki dan perempuan hampir seimbang dan dropout lebih tinggi terjadi pada kelas pagi (85,4%).
  
![image](https://github.com/user-attachments/assets/6e6d314f-3cdb-4f18-845c-9fc82d9c1229)
![image](https://github.com/user-attachments/assets/6a6e2590-a592-4e66-914b-75f099794d0f)

- **Pengaruh Program Studi:** Program Manajemen (evening attendance), Keperawatan, dan Jurnalistik memiliki jumlah dropout tertinggi.
![image](https://github.com/user-attachments/assets/ea5d5081-377f-4e55-b809-aa843a17bbc5)

- **Status Sosial:** Mahasiswa lajang mendominasi jumlah dropout dibanding status pernikahan lainnya.
![image](https://github.com/user-attachments/assets/0d30ab5c-49b4-4cc9-92f3-677940d2b28b)

- **Mahasiswa Internasional:** Dropout juga terjadi pada mahasiswa internasional, namun dalam jumlah lebih kecil dibanding mahasiswa lokal.
![image](https://github.com/user-attachments/assets/cd953e3c-034b-47c1-ae8b-514b82262e18)

## Menjalankan Sistem Machine Learning
Prototype model prediksi dropout dikembangkan menggunakan Streamlit dan sudah dideploy ke Streamlit Community Cloud.

Aplikasi ini memungkinkan user untuk:
- Memasukkan data baru mahasiswa
- Melihat prediksi apakah mahasiswa tersebut berpotensi dropout atau tidak

**Cara menjalankan secara lokal:**

Sebelumnya pastikan sudah **setup environment** seperti langkah di atas kemudian jalankan perintah berikut:
```
streamlit run app.py
```

**Akses online:**
🔗 [Streamlit App - Dropout Predictor](https://dropout-prediction-jaya-jaya-institut.streamlit.app/)

**Cara Menggunakan Aplikasi**
- Buka aplikasi melalui tautan di atas.
- Isi seluruh data mahasiswa pada form input yang tersedia di sidebar kiri, seperti nilai semester, status beasiswa, jumlah mata kuliah yang diambil/disetujui, dan lainnya.
- Setelah semua data terisi, klik tombol "Prediksi Dropout" di bagian bawah sidebar.
- Hasil prediksi akan langsung ditampilkan di bagian utama (main panel) aplikasi, menunjukkan apakah mahasiswa tersebut berpotensi melakukan dropout atau tidak.

## Conclusion
Berdasarkan analisis data performa mahasiswa dari Jaya Jaya Institut, kami menemukan bahwa dropout dipengaruhi oleh berbagai faktor akademik, administratif, dan sosial.

Beberapa temuan penting:
- **Performa Akademik:** Mahasiswa dengan jumlah mata kuliah yang lulus (approved) rendah di semester 1 dan 2 memiliki risiko tinggi untuk dropout. 
- **Status Keuangan:** Fakta menarik dari dashboard menunjukkan bahwa mayoritas mahasiswa dropout (67%) justru telah melunasi UKT-nya, menandakan bahwa dropout bukan disebabkan oleh faktor keuangan utama, melainkan bisa jadi karena motivasi, beban akademik, atau faktor eksternal lainnya.
- **Status Beasiswa:** Sebagian besar mahasiswa dropout bukan penerima beasiswa, yang tetap menunjukkan bahwa dukungan finansial mungkin memberi sedikit proteksi terhadap dropout, namun bukan faktor utama.
- **Pola Kehadiran (Siang/Malam):** Mayoritas mahasiswa dropout berasal dari kelas siang/pagi (85.4%), namun hal ini perlu dikaji berdasar proporsi total mahasiswa tiap kelompok.
- **Gender dan Program Studi:** Mahasiswa laki-laki cenderung sedikit lebih banyak dropout, dan beberapa jurusan seperti Manajemen, Keperawatan, dan Jurnalistik menunjukkan tingkat dropout yang tinggi.

Dengan memahami karakteristik umum mahasiswa yang berisiko dropout, institusi dapat mengambil tindakan preventif secara lebih terarah dan efisien. Hal ini diharapkan mampu menurunkan angka dropout dan meningkatkan kualitas layanan pendidikan di Jaya Jaya Institut secara menyeluruh.

### Rekomendasi Action Items

Berikut adalah beberapa langkah yang dapat dilakukan oleh Jaya Jaya Institut berdasarkan hasil proyek ini:
- **Lakukan intervensi dini** terhadap mahasiswa dengan performa akademik rendah, terutama yang hanya menyelesaikan sedikit mata kuliah atau memiliki nilai rendah di semester awal.
- **Pantau lebih ketat** mahasiswa yang bukan penerima beasiswa dan yang menunggak pembayaran, karena kelompok ini cenderung memiliki risiko dropout yang lebih tinggi.
- **Tingkatkan pendampingan** pada program studi dengan tingkat dropout tinggi seperti Manajemen, Keperawatan, dan Jurnalistik, dengan menghadirkan program mentoring atau konseling rutin.
- **Integrasikan sistem prediksi dropout** ke sistem akademik untuk mengirimkan notifikasi otomatis kepada dosen wali terhadap mahasiswa dengan risiko tinggi.
- **Sesuaikan dukungan keuangan** seperti pemberian beasiswa tambahan atau relaksasi UKT bagi mahasiswa yang berisiko tinggi dropout namun sudah menunjukkan usaha akademik.


