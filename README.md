# Setup Environment

## Menggunakan Anaconda

Buat virtual environment baru menggunakan conda:

```bash
conda create --name bike-sharing-env python=3.9
```

Aktifkan environment:

```bash
conda activate bike-sharing-env
```

Install seluruh dependency:

```bash
pip install -r requirements.txt
```

---

## Menggunakan Terminal / Virtual Environment Biasa

Buat folder project:

```bash
mkdir submission
cd submission
```

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment:

### Windows
```bash
venv\Scripts\activate
```

### MacOS / Linux
```bash
source venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

# Menjalankan Notebook

Jalankan Jupyter Notebook:

```bash
jupyter notebook
```

Kemudian buka file:

```text
notebook.ipynb
```

---

# Menjalankan Dashboard Streamlit

Pastikan terminal berada pada root project:

```text
submission/
```

Lalu jalankan:

```bash
streamlit run dashboard/dashboard.py
```