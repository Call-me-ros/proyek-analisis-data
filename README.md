# E-Commerce Data Analysis Project

## Project Overview

Proyek ini bertujuan untuk menganalisis data transaksi e-commerce guna mendapatkan wawasan strategis mengenai performa bisnis. Fokus utama analisis ini adalah pada identifikasi kontribusi pendapatan berdasarkan geografis dan analisis volume penjualan kategori produk untuk mendukung pengambilan keputusan operasional.

---

## Business Questions (SMART)

1. **Revenue Analysis:** Negara bagian (`customer_state`) mana yang memberikan kontribusi total pendapatan (`revenue`) tertinggi dari pesanan berstatus `delivered` selama tahun 2018 untuk menentukan prioritas efisiensi distribusi?

2. **Product Performance:** Apa saja 5 kategori produk dengan volume penjualan terbanyak selama periode 2017–2018 dan bagaimana kontribusinya terhadap total pendapatan guna mengoptimalkan manajemen stok inventaris?

---

## Tech Stack

| Komponen  | Detail                                   |
|-----------|------------------------------------------|
| Language  | Python                                   |
| Libraries | Pandas, Matplotlib, Seaborn, Streamlit, Babel |

---

## Project Structure

```
submission_analisis_data/
├── dashboard/
│   ├── dashboard.py       # File utama Streamlit dashboard
│   └── all_data.csv       # Dataset yang telah diproses
├── data/                  # Dataset mentah (raw data) dalam format CSV
├── notebook.ipynb         # Dokumentasi lengkap: Wrangling, EDA, Visualisasi
├── requirements.txt       # Daftar library Python yang diperlukan
└── README.md              # Dokumentasi proyek
```

---

## Setup Environment

### Option 1: Terminal / Command Prompt (Recommended)

1. Buat folder proyek dan masuk ke direktori tersebut:

   ```bash
   mkdir submission_analisis_data
   cd submission_analisis_data
   ```

2. Buat Virtual Environment:

   ```bash
   python -m venv venv
   ```

3. Aktifkan Virtual Environment:

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install semua library yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

---

### Option 2: Conda

```bash
conda create --name main-ds python=3.12
conda activate main-ds
pip install -r requirements.txt
```

---

## Run Streamlit Dashboard

Setelah environment siap, jalankan dashboard dengan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

---

## Author

**Piros**
