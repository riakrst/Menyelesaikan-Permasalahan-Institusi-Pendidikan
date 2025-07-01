import sys
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Mapping data
marital_status_dict = {
    "lajang": 1,
    "menikah": 2,
    "duda/janda": 3,
    "cerai": 4,
    "kumpul kebo": 5,
    "pisah hukum": 6
}

application_mode_dict = {
    "fase ke-1 - kontingen umum": 1,
    "Ordonansi No. 612/93": 2,
    "fase ke-1 - kontingen khusus (Kepulauan Azores)": 5,
    "Pemegang kursus tinggi lainnya": 7,
    "Ordonansi No. 854-B/99": 10,
    "Mahasiswa internasional (sarjana)": 15,
    "fase ke-1 - kontingen khusus (Pulau Madeira)": 16,
    "fase ke-2 - kontingen umum": 17,
    "fase ke-3 - kontingen umum": 18,
    "Ordonansi No. 533-A/99, item b2) (Rencana Berbeda)": 26,
    "Ordonansi No. 533-A/99, item b3 (Institusi Lain)": 27,
    "Di atas 23 tahun": 39,
    "Transfer": 42,
    "Ganti jurusan": 43,
    "Pemegang diploma spesialisasi teknologi": 44,
    "Ganti institusi/jurusan": 51,
    "Pemegang diploma siklus pendek": 53,
    "Ganti institusi/jurusan (Internasional)": 57
}

course_dict = {
    "Teknologi Produksi Biofuel": 33,
    "Desain Animasi dan Multimedia": 171,
    "Layanan Sosial (kehadiran malam)": 8014,
    "Agronomi": 9003,
    "Desain Komunikasi": 9070,
    "Keperawatan Veteriner": 9085,
    "Teknik Informatika": 9119,
    "Equinkultur": 9130,
    "Manajemen": 9147,
    "Layanan Sosial": 9238,
    "Pariwisata": 9254,
    "Keperawatan": 9500,
    "Kebersihan Mulut": 9556,
    "Manajemen Periklanan dan Pemasaran": 9670,
    "Jurnalisme dan Komunikasi": 9773,
    "Pendidikan Dasar": 9853,
    "Manajemen (kehadiran malam)": 9991
}

daytime_evening_dict = {
    "siang hari": 1,
    "malam hari": 0
}

previous_qualification_dict = {
    "Pendidikan menengah": 1,
    "Pendidikan tinggi - gelar sarjana": 2,
    "Pendidikan tinggi - gelar": 3,
    "Pendidikan tinggi - master": 4,
    "Pendidikan tinggi - doktor": 5,
    "Frekuensi pendidikan tinggi": 6,
    "Tahun ke-12 sekolah - tidak selesai": 9,
    "Tahun ke-11 sekolah - tidak selesai": 10,
    "Lainnya - tahun ke-11 sekolah": 12,
    "Tahun ke-10 sekolah": 14,
    "Tahun ke-10 sekolah - tidak selesai": 15,
    "Pendidikan dasar siklus ke-3 (tahun ke-9/10/11) atau setara": 19,
    "Pendidikan dasar siklus ke-2 (tahun ke-6/7/8) atau setara": 38,
    "Kursus spesialisasi teknologi": 39,
    "Pendidikan tinggi - gelar (siklus ke-1)": 40,
    "Kursus teknis tinggi profesional": 42,
    "Pendidikan tinggi - master (siklus ke-2)": 43
}

nacionality_dict = {
    "Portugis": 1, "Jerman": 2, "Spanyol": 6, "Italia": 11, "Belanda": 13, "Inggris": 14,
    "Lithuania": 17, "Angola": 21, "Cape Verde": 22, "Guinea": 24, "Mozambik": 25,
    "Santome": 26, "Turki": 32, "Brasil": 41, "Rumania": 62, "Moldova (Republik)": 100,
    "Meksiko": 101, "Ukraina": 103, "Rusia": 105, "Kuba": 108, "Kolombia": 109
}

# Untuk mother_qualification dan father_qualification kita bisa pakai mapping yang sama
mothers_qualification_dict = fathers_qualification_dict = {
    "Pendidikan Menengah - Tahun ke-12 Sekolah atau Setara": 1,
    "Pendidikan Tinggi - Gelar Sarjana": 2,
    "Pendidikan Tinggi - Gelar": 3,
    "Pendidikan Tinggi - Master": 4,
    "Pendidikan Tinggi - Doktor": 5,
    "Frekuensi Pendidikan Tinggi": 6,
    "Tahun ke-12 Sekolah - Tidak Selesai": 9,
    "Tahun ke-11 Sekolah - Tidak Selesai": 10,
    "Tahun ke-7 (Lama)": 11,
    "Lainnya - Tahun ke-11 Sekolah": 12,
    "Tahun ke-10 Sekolah": 14,
    "Kursus perdagangan umum": 18,
    "Pendidikan Dasar Siklus ke-3 (Tahun ke-9/10/11) atau Setara": 19,
    "Kursus teknis-profesional": 22,
    "Tahun ke-7 sekolah": 26,
    "Siklus ke-2 kursus sekolah menengah umum": 27,
    "Tahun ke-9 Sekolah - Tidak Selesai": 29,
    "Tahun ke-8 sekolah": 30,
    "Tidak diketahui": 34,
    "Tidak bisa baca tulis": 35,
    "Bisa baca tanpa tahun ke-4 sekolah": 36,
    "Pendidikan dasar siklus ke-1 (tahun ke-4/5) atau setara": 37,
    "Pendidikan Dasar Siklus ke-2 (Tahun ke-6/7/8) atau Setara": 38,
    "Kursus spesialisasi teknologi": 39,
    "Pendidikan tinggi - gelar (siklus ke-1)": 40,
    "Kursus studi tinggi khusus": 41,
    "Kursus teknis tinggi profesional": 42,
    "Pendidikan Tinggi - Master (siklus ke-2)": 43,
    "Pendidikan Tinggi - Doktor (siklus ke-3)": 44
}

mothers_occupation_dict = fathers_occupation_dict = {
    "Mahasiswa": 0,
    "Perwakilan Kekuasaan Legislatif dan Badan Eksekutif, Direktur, Direktur dan Manajer Eksekutif": 1,
    "Spesialis dalam Kegiatan Intelektual dan Ilmiah": 2,
    "Teknisi Tingkat Menengah dan Profesi": 3,
    "Staf administratif": 4,
    "Layanan Pribadi, Pekerja Keamanan dan Keselamatan dan Penjual": 5,
    "Petani dan Pekerja Terampil di Pertanian, Perikanan dan Kehutanan": 6,
    "Pekerja Terampil di Industri, Konstruksi dan Pengrajin": 7,
    "Operator Instalasi dan Mesin dan Pekerja Perakitan": 8,
    "Pekerja Tidak Terampil": 9,
    "Profesi Angkatan Bersenjata": 10,
    "Profesional kesehatan": 122,
    "Guru": 123,
    "Spesialis dalam teknologi informasi dan komunikasi (TIK)": 125,
    "Teknisi dan profesi tingkat menengah sains dan teknik": 131,
    "Teknisi dan profesional, tingkat menengah kesehatan": 132,
    "Teknisi tingkat menengah dari layanan hukum, sosial, olahraga, budaya dan serupa": 134,
    "Pekerja kantor, sekretaris secara umum dan operator pemrosesan data": 141,
    "Operator terkait data, akuntansi, statistik, layanan keuangan dan registri": 143,
    "Pekerja layanan pribadi": 151,
    "Penjual": 152,
    "Pekerja kebersihan": 191,
    "Asisten persiapan makanan": 194
}

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Prediksi Dropout Siswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS untuk styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        text-align: left;
        margin-bottom: 2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Model
model = joblib.load('model/xgboost_dropout_model.joblib')
scaler = joblib.load('model/scaler.joblib')
feature_order = joblib.load('model/feature_order.joblib')


st.markdown('<div class="main-header">🎓📉 Prediksi Risiko Dropout Mahasiswa Jaya Jaya Institut</div>', unsafe_allow_html=True)

# Input dari sidebar
st.sidebar.header("Input Data Siswa")
marital_status = st.sidebar.selectbox("Status Pernikahan", list(marital_status_dict.keys()))
gender_label = st.sidebar.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
gender = 1 if gender_label == "Laki-laki" else 0
age = st.sidebar.slider("Usia saat Mendaftar", 17, 70, 20)
nacionality = st.sidebar.selectbox("Kewarganegaraan", list(nacionality_dict.keys()))
application_mode = st.sidebar.selectbox("Mode Aplikasi", list(application_mode_dict.keys()))
application_order = st.sidebar.slider("Urutan Aplikasi", 0, 9, 1)
course = st.sidebar.selectbox("Program Studi", list(course_dict.keys()))
daytime_label = st.sidebar.selectbox("Waktu Kuliah", ["Malam", "Siang"])
daytime_evening = 1 if daytime_label == "Siang" else 0
prev_qualification = st.sidebar.selectbox("Kualifikasi Sebelumnya", list(previous_qualification_dict.keys()))
prev_qual_grade = st.sidebar.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 150.0, 1.0)
admission_grade = st.sidebar.slider("Nilai Penerimaan", 0.0, 200.0, 150.0, 1.0)
mothers_qual = st.sidebar.selectbox("Kualifikasi Ibu", list(mothers_qualification_dict.keys()))
fathers_qual = st.sidebar.selectbox("Kualifikasi Ayah", list(fathers_qualification_dict.keys()))
mothers_occ = st.sidebar.selectbox("Pekerjaan Ibu", list(mothers_occupation_dict.keys()))
fathers_occ = st.sidebar.selectbox("Pekerjaan Ayah", list(fathers_occupation_dict.keys()))

displaced_label = st.sidebar.selectbox("Status Pengungsi", ["Tidak", "Ya"])
displaced = 1 if displaced_label == "Ya" else 0

ed_needs_label = st.sidebar.selectbox("Kebutuhan Khusus", ["Tidak", "Ya"])
ed_special_needs = 1 if ed_needs_label == "Ya" else 0

debtor_label = st.sidebar.selectbox("Status Hutang", ["Tidak", "Ya"])
debtor = 1 if debtor_label == "Ya" else 0

tu_fee_label = st.sidebar.selectbox("Status SPP", ["Belum Diperbarui", "Terkini"])
tu_fee_up = 1 if tu_fee_label == "Terkini" else 0

scholar_label = st.sidebar.selectbox("Penerima Beasiswa", ["Tidak", "Ya"])
scholarship = 1 if scholar_label == "Ya" else 0

intl_label = st.sidebar.selectbox("Mahasiswa Internasional", ["Tidak", "Ya"])
international = 1 if intl_label == "Ya" else 0

unemployment = st.sidebar.number_input("Tingkat Pengangguran", 0.0, 50.0, 10.8)
gdp = st.sidebar.number_input("GDP", -10.0, 10.0, 1.74)


# Input tambahan fitur penting
st.sidebar.subheader("Data Akademik")
cu_1st_credited = st.sidebar.slider("SKS Semester 1 (Credited)", 0, 100, 6)
cu_1st_enrolled = st.sidebar.slider("Mata Kuliah Semester 1 (Enrolled)", 0, 100, 6)
cu_1st_approved = st.sidebar.slider("Mata Kuliah Lulus Semester 1 (Approved)", 0, 100, 6)
cu_1st_wo_eval = st.sidebar.slider("Tanpa Evaluasi Semester 1", 0, 10, 0)
cu_2nd_credited = st.sidebar.slider("SKS Semester 2 (Credited)", 0, 100, 6)
cu_2nd_enrolled = st.sidebar.slider("Mata Kuliah Semester 2 (Enrolled)", 0, 100, 6)
cu_2nd_approved = st.sidebar.slider("Mata Kuliah Lulus Semester 2 (Approved)", 0, 100, 6)
cu_2nd_grade = st.sidebar.slider("Rata-rata Nilai Semester 2", 0.0, 20.0, 13.9, 0.1)


# Tombol prediksi
if st.sidebar.button("Prediksi Dropout"):
    input_data = {
        'Marital_status': marital_status_dict[marital_status],
        'Application_mode': application_mode_dict[application_mode],
        'Application_order': application_order,
        'Course': course_dict[course],
        'Daytime_evening_attendance': daytime_evening,
        'Previous_qualification': previous_qualification_dict[prev_qualification],
        'Previous_qualification_grade': prev_qual_grade,
        'Admission_grade': admission_grade,
        'Nacionality': nacionality_dict[nacionality],
        'Mothers_qualification': mothers_qualification_dict[mothers_qual],
        'Fathers_qualification': fathers_qualification_dict[fathers_qual],
        'Mothers_occupation': mothers_occupation_dict[mothers_occ],
        'Fathers_occupation': fathers_occupation_dict[fathers_occ],
        'Displaced': displaced,
        'Educational_special_needs': ed_special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tu_fee_up,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': international,
        'Curricular_units_1st_sem_credited': cu_1st_credited,
        'Curricular_units_1st_sem_enrolled': cu_1st_enrolled,
        'Curricular_units_1st_sem_approved': cu_1st_approved,
        'Curricular_units_1st_sem_without_evaluations': cu_1st_wo_eval,
        'Curricular_units_1st_sem_grade': 13.9,
        'Curricular_units_2nd_sem_credited': cu_2nd_credited,
        'Curricular_units_2nd_sem_enrolled': cu_2nd_enrolled,
        'Curricular_units_2nd_sem_approved': cu_2nd_approved,
        'Curricular_units_2nd_sem_grade': cu_2nd_grade,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Target': 13.9,
        'Inflation_rate': 0.3,
        'Unemployment_rate': unemployment,
        'GDP': gdp
    }

    # Buat DataFrame dan susun urutan kolom
    df_input = pd.DataFrame([input_data])
    df_input = df_input.reindex(columns=feature_order)

    # Scaling
    df_scaled = scaler.transform(df_input)

    # Prediksi
    pred = model.predict(df_scaled)[0]
    prob = model.predict_proba(df_scaled)[0][1]

    # Output
    st.subheader("Hasil Prediksi")
    st.write(f"**Prediksi:** {'Dropout' if pred == 1 else 'Tidak Dropout'}")
    st.write(f"**Probabilitas:** {prob:.2%}")

    if prob >= 0.7:
        st.warning("⚠️ Risiko tinggi dropout! Perlu tindakan cepat.")
    elif prob >= 0.4:
        st.info("🟡 Risiko sedang. Perlu pemantauan.")
    else:
        st.success("🟢 Risiko rendah. Pertahankan performa siswa.")
