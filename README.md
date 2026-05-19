# Bike Sharing Data Analysis Project

## Deskripsi Project

Project ini merupakan proyek analisis data menggunakan Bike Sharing Dataset.  
Analisis dilakukan untuk memahami pola penyewaan sepeda berdasarkan kondisi cuaca dan waktu penyewaan.

Project ini dibuat menggunakan:
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

---

# Struktur Direktori Project

```text
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

# Penjelasan Folder dan File

## 1. Folder `dashboard/`

Folder ini digunakan untuk dashboard interaktif menggunakan Streamlit.

### `dashboard.py`
Berisi source code dashboard Streamlit untuk menampilkan:
- visualisasi data
- filter data
- insight hasil analisis

### `main_data.csv`
Dataset utama yang telah dibersihkan dan digunakan oleh dashboard.

---

## 2. Folder `data/`

Berisi dataset mentah yang digunakan dalam proses analisis.

### `day.csv`
Dataset penyewaan sepeda berdasarkan hari.

### `hour.csv`
Dataset penyewaan sepeda berdasarkan jam.

---

## 3. `notebook.ipynb`

Notebook utama yang berisi:
- business understanding
- data wrangling
- exploratory data analysis
- visualization
- conclusion
- recommendation

---

## 4. `requirements.txt`

Berisi library Python yang digunakan dalam project.

---

## 5. `url.txt`

Berisi link deployment dashboard Streamlit Cloud.

---

# Business Questions

## Pertanyaan Bisnis 1
Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda pada tahun 2011–2012?

## Pertanyaan Bisnis 2
Pada jam berapa jumlah penyewaan sepeda mencapai puncak tertinggi selama periode 2011–2012?

---

# Insight Hasil Analisis

## Insight 1
Kondisi cuaca sangat memengaruhi jumlah penyewaan sepeda.  
Cuaca cerah menghasilkan jumlah penyewaan tertinggi.

## Insight 2
Jumlah penyewaan sepeda paling tinggi terjadi pada pagi dan sore hari, terutama saat jam sibuk.

---

# Library yang Digunakan

```text
pandas
numpy
matplotlib
seaborn
streamlit
```

---

# Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone https://github.com/username/repository-name.git
```

---

## 2. Masuk ke Folder Project

```bash
cd repository-name
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Cara Menjalankan Dashboard Streamlit

Pastikan terminal berada di root project:

```text
submission/
```

Lalu jalankan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

---

# Tampilan Dashboard

Dashboard menampilkan:
- dataset preview
- visualisasi pengaruh cuaca
- visualisasi penyewaan per jam
- insight hasil analisis
- filter jam penyewaan

---

# Deployment Streamlit

Dashboard dapat diakses melalui:

```text
https://your-streamlit-url.streamlit.app
```

---

# Author

Nama: Giri Firmansyah

Project dibuat untuk submission kelas Analisis Data Dicoding.