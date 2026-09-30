"""
=====================================================
 Columnar Transposition Cipher - Cipher Transposisi
 Materi: 03 - Ragam Cipher Klasik Bagian 1
 Ref     : Dr. Ir. Rinaldi Munir (STEI ITB, 2025)
=====================================================
Prinsip : Plainteks dituliskan HORIZONTAL per baris ke
          dalam matriks berukuran m baris x n kolom,
          dengan n = panjang kata kunci. Cipherteks
          dibaca VERTIKAL kolom demi kolom, dimulai
          dari kolom yang huruf kuncinya paling awal
          dalam urutan alfabet (slide hal. 40-42).

Langkah enkripsi:
  1. Buang spasi dari plainteks.
  2. Tulis pesan horizontal pada matriks m x n.
  3. Pad kan sel kosong terakhir dengan 'X'.
  4. Beri peringkat (rank) tiap huruf kunci sesuai
     urutan alfabet; huruf sama diberi rank berurutan.
  5. Baca cipherteks vertikal mengikuti rank 1, 2, ...
"""

def _key_ranks(keyword: str) -> list:
    """Mengembalikan urutan pembacaan kolom (rank) untuk keyword.
    Contoh: TOMBAK -> huruf A,B,K,M,O,T bernilai 1..6
    sehingga rank kolom = [6, 5, 4, 2, 1, 3] (untuk T,O,M,B,A,K)."""
    indexed = sorted(enumerate(keyword.upper()),
                     key=lambda x: (x[1], x[0]))
    ranks = [0] * len(keyword)
    for rank, (col, _) in enumerate(indexed, start=1):
        ranks[col] = rank
    return ranks


def columnar_encrypt(plainteks: str, keyword: str) -> str:
    n = len(keyword)
    teks = "".join(ch for ch in plainteks.upper() if ch.isalpha())
    # padding 'X' agar panjang kelipatan n
    pad = (-len(teks)) % n
    teks += "X" * pad

    # tulis horizontal: baris demi baris
    rows = [teks[i:i + n] for i in range(0, len(teks), n)]

    # baca vertikal sesuai rank kolom 1..n
    ranks = _key_ranks(keyword)
    cipherteks = ""
    for r in range(1, n + 1):
        col = ranks.index(r)
        cipherteks += "".join(row[col] for row in rows)
    return cipherteks


def columnar_decrypt(cipherteks: str, keyword: str) -> str:
    n = len(keyword)
    teks = "".join(ch for ch in cipherteks.upper() if ch.isalpha())
    m = len(teks) // n                      # jumlah baris
    ranks = _key_ranks(keyword)

    # potong cipherteks per kolom (sesuai rank 1..n)
    cols = {}
    idx = 0
    for r in range(1, n + 1):
        col = ranks.index(r)
        cols[col] = teks[idx: idx + m]
        idx += m

    # baca horizontal baris demi baris -> plainteks
    plainteks = ""
    for i in range(m):
        for col in range(n):
            plainteks += cols[col][i]
    return plainteks


def main():
    print("=" * 55)
    print("   COLUMNAR TRANSPOSITION CIPHER (kunci: kata)")
    print("=" * 55)
    while True:
        print("\nMenu:\n1. Enkripsi\n2. Dekripsi\n3. Keluar")
        pilihan = input("Pilih menu (1-3): ").strip()
        if pilihan == "1":
            pesan = input("Ketikkan pesan   : ")
            kunci = input("Kata kunci       : ")
            print(f"Cipherteks       : {columnar_encrypt(pesan, kunci)}")
        elif pilihan == "2":
            pesan = input("Ketikkan cipherteks: ")
            kunci = input("Kata kunci         : ")
            print(f"Plainteks (pad X)  : {columnar_decrypt(pesan, kunci)}")
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


# Contoh pengujian (slide hal. 42):
# plainteks "PURWAKARTA", kunci "TOMBAK"
if __name__ == "__main__":
    contoh = "PURWAKARTA"
    kunci = "TOMBAK"
    c = columnar_encrypt(contoh, kunci)
    print(f"[TEST] Plainteks : {contoh}")
    print(f"[TEST] Kunci     : {kunci}")
    print(f"[TEST] Cipherteks: {c}")
    d = columnar_decrypt(c, kunci)
    assert d.rstrip("X") == contoh.replace(" ", "").upper(), "Dekripsi gagal!"
    print(f"[TEST] Dekripsi  : {d} (OK)\n")
    main()
