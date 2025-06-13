# 🎨 Digital Art Studio – Computer Graphics 24/25

Sebuah aplikasi menggambar digital interaktif berbasis **Python** dan **Pygame**, dikembangkan sebagai bagian dari tugas mata kuliah **Grafika Komputer**.

Antarmuka aplikasi ini didesain modern dan responsif, memungkinkan pengguna untuk menggambar secara bebas dengan berbagai bentuk dan pilihan warna yang menarik.

---

## 🖼️ Fitur Utama

✅ **Mode Menggambar:**

- 🟣 **Titik**
- 🔵 **Garis**
- ✏️ **Draw Bebas**
- 🔲 **Persegi**
- ⚪ **Lingkaran**
- 🥚 **Elips**

✅ **Palet Warna Cantik:**

- Tersedia 10 warna menarik dalam tampilan bulat
- Klik untuk memilih warna yang akan digunakan

✅ **Antarmuka Interaktif:**

- Tombol **mode menggambar** yang stylish
- Tombol 🗑️ **Hapus** untuk membersihkan kanvas
- Tombol 💾 **Simpan** untuk menyimpan hasil gambar sebagai file `.png`

✅ **UI Modern:**

- Gradien warna pada background toolbar
- Shadow & border radius pada tombol
- Feedback hover & indikator terpilih

✅ **Live Preview** saat menggambar bentuk garis, persegi, lingkaran, dan elips

---

## 📦 Requirements

- Python **3.8+**
- Pygame **2.x**

---

## 💻 Cara Menjalankan

1. Pastikan Python dan `pygame` sudah terpasang:

   ```bash
   pip install pygame
   ```

2. Jalankan program:
   ```bash
   python main.py
   ```

---

## 💾 Cara Menyimpan Gambar

Klik tombol **"💾 Simpan"** untuk menyimpan hasil gambar. File akan disimpan dengan nama:

```
gambar_saya.png
```

di direktori yang sama dengan file `.py`.

---

## 📸 Tampilan Aplikasi

> ![Tampilan Aplikasi](screenshot.png)  
> _UI stylish dan intuitif, dengan gradient, tombol bulat, dan shadow untuk pengalaman menggambar digital yang lebih modern._

---

## 👨‍🎓 Dibuat Oleh

> Nama Mahasiswa  
> **Universitas Muhammadiyah Malang**  
> Mata Kuliah: _Grafika Komputer 24/25_  
> Dosen Pengampu: [Isi Nama Dosen jika perlu]

---

## 📝 Catatan

- Aplikasi ini belum memiliki fitur undo/redo.
- Fitur ekspor nama file belum dinamis (default: `gambar_saya.png`).
- Semua komponen dibuat manual menggunakan pygame (tidak menggunakan UI library eksternal).
