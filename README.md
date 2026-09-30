# Tugas Kriptografi — Implementasi Cipher Klasik (Python)

Repositori ini berisi implementasi **3 algoritma Cipher Klasik** dalam bahasa **Python 3**,
dikerjakan sebagai tugas mata kuliah **Kriptografi**. 

> Kriptografi klasik adalah kriptografi kunci-simetri yang memproses pesan berupa huruf
> alfabet saja, menggunakan dua teknik dasar: **substitusi** dan **transposisi**
> (kombinasi keduanya disebut *product cipher* / super-enkripsi).

---

## 📁 Daftar Berkas

| Berkas | Kategori Cipher | Kunci |
|---|---|---|
| `1_caesar_cipher.py` | Substitusi abjad-tunggal (*monoalphabetic*) | Bilangan `k` (0–25) |
| `2_columnar_transposition.py` | Transposisi (*permutation*) | Kata kunci (mis. `TOMBAK`) |
| `3_rail_fence.py` | Transposisi zig-zag | Bilangan rail `k` (≥ 2) |

---

## 1️⃣ Caesar Cipher — `1_caesar_cipher.py`

- **Kategori:** Cipher Substitusi Abjad-Tunggal (*Monoalphabetic Substitution Cipher*).
- **Prinsip:** Setiap huruf *plainteks* digantikan oleh huruf lain yang berjarak `k`
  posisi ke kanan dalam urutan alfabet.
- **Formulasi matematika** (`p`, `c` ∈ [0, 25], dengan A=0 … Z=25):

  $$c = E(p) = (p + k) \bmod 26 \qquad p = D(c) = (c - k) \bmod 26$$

- **Fitur program:**
  - Enkripsi & dekripsi (huruf besar/kecil dipertahankan, karakter non-alfabet dibiarkan).
  - **Brute force (exhaustive key search)** — Caesar Cipher mudah dipecahkan karena
    hanya ada 26 kunci (slide hal. 21–24). Program dapat mencoba semua `k = 0..25`.

### Contoh Pengujian

```text
Plainteks : KRIPTOGRAFI
Kunci (k) : 3
Cipherteks: NULSWRJUDIL
Dekripsi  : KRIPTOGRAFI   ✓
```

Contoh lain (slide hal. 10–12): `awasi asterix dan temannya obelix` dengan `k = 3`
→ `DZDVL DVWHULA GDQ WHPDQQBA REHOLA`

> 💡 **ROT13** adalah kasus khusus Caesar dengan `k = 13` — enkripsi = dekripsi,
> sebab `ROT13(ROT13(x)) = x` (slide hal. 26–27).

---

## 2️⃣ Columnar Transposition Cipher — `2_columnar_transposition.py`

- **Kategori:** Cipher Transposisi (*Permutation Cipher*) — posisi huruf diubah,
  bukan hurufnya.
- **Prinsip:** Plainteks dituliskan **horizontal** per baris pada matriks
  `m × n` (`n` = panjang kata kunci), lalu dibaca **vertikal** kolom demi kolom,
  dimulai dari kolom yang huruf kuncinya paling awal dalam alfabet (slide hal. 40–42).
- **Langkah enkripsi:**
  1. Buang spasi dari plainteks.
  2. Tulis pesan horizontal pada matriks `m × n`.
  3. Pad kan sel kosong (ditandai `X`).
  4. Beri peringkat tiap huruf kunci sesuai urutan alfabet
     (huruf yang sama diberi peringkat berurutan).
  5. Baca cipherteks vertikal mengikuti peringkat 1, 2, 3, …

### Contoh Pengujian

```text
Plainteks : PURWAKARTA
Kata kunci: TOMBAK
Matriks (padding X):
  P U R W A K
  A R T A X X
Urutan baca kolom (berdasarkan A<B<K<M<O<T): kolom 5, 4, 6, 3, 2, 1
Cipherteks: AXWAKXRTURPA
Dekripsi  : PURWAKARTAXX → buang padding X → PURWAKARTA   ✓
```

Contoh dari slide (hal. 42): `sistem dan teknologi informasi itb` dengan kunci `TOMBAK`
→ `EEGRTTTOOIMKIMBSNLFIIAONSSDNIA` — **hasil program identik dengan slide**.

---

## 3️⃣ Rail Fence Transposition Cipher — `3_rail_fence.py`

- **Kategori:** Cipher Transposisi dengan pola **zig-zag** (slide hal. 44).
- **Prinsip:** Karakter plainteks dituliskan secara diagonal naik-turun pada `k`
  baris (*rails*), lalu cipherteks dibaca **baris demi baris** dari atas ke bawah.
- **Fitur program:**
  - Enkripsi & dekripsi.
  - **Visualisasi zig-zag** di terminal (meniru ilustrasi pada slide).

### Contoh Pengujian

```text
Plainteks : TEKNIKINFORMATIKA
Rail (k)  : 3

Visual zig-zag:
  T . . . I . . . F . . . A . . . A
  . E . N . K . N . O . M . T . K .
  . . K . . . I . . . R . . . I . .

Cipherteks: TIFAAENKNOMTKKIRI
Dekripsi  : TEKNIKINFORMATIKA   ✓
```

Contoh dari slide (hal. 44): `CRYPTOGRAPHY AND DATA SECURITY` dengan `k = 3`
→ `CTAAAEIRPORPYNDTSCRTYGHDAUY` — **hasil program identik dengan slide**.

---

## 🧪 Kriptanalisis (Ringkasan dari Materi)

| Cipher | Kelemahan utama | Teknik pemecahan |
|---|---|---|
| Caesar | Ruang kunci hanya 26 | *Exhaustive key search* (brute force) — sudah tersedia di program |
| Monoalphabetic | Statistik huruf plainteks tercermin di cipherteks | Analisis frekuensi huruf/bigram/trigram (E≈12,7% dalam Bahasa Inggris; A≈17,5% dalam Bahasa Indonesia) |
| Transposisi | Pola permutasi dapat ditebak dengan coba-cola | Analisis frekuensi + terkaan kata |

---

## 🚀 Cara Menjalankan

Persyaratan: **Python 3.x** (tanpa library tambahan).

```bash
# 1. Clone repositori
git clone https://github.com/<username-github>/tugas-kriptografi-cipher.git
cd tugas-kriptografi-cipher

# 2. Jalankan masing-masing program
python 1_caesar_cipher.py
python 2_columnar_transposition.py
python 3_rail_fence.py
```

Setiap program menampilkan **menu interaktif** (Enkripsi / Dekripsi / Keluar),
dan akan menjalankan contoh uji otomatis (dengan `assert`) terlebih dahulu
agar hasilnya bisa langsung dicocokkan dengan materi kuliah.

---

## 👤 Identitas Mahasiswa

- **Nama:** Muhammad Hafizh Alfauzi
- **NIM:** 312410501
- **Mata Kuliah:** Kriptografi
- **Program Studi:** Teknik Informatika
- **Referensi:** 02 Ragam Cipher Klasik
