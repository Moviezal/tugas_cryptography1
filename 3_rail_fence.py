"""
=====================================================
 Rail Fence Transposition Cipher - Cipher Transposisi
 Materi: 03 - Ragam Cipher Klasik Bagian 1
 Ref     : Dr. Ir. Rinaldi Munir (STEI ITB, 2025)
=====================================================
Prinsip : Karakter plainteks dituliskan secara DIAGONAL
          mengikuti pola zig-zag (naik-turun) pada k
          baris (rail). Cipherteks dibaca BARIS DEMI BARIS
          dari atas ke bawah (slide hal. 44).

Langkah enkripsi:
  1. Buat k "rel" (baris).
  2. Tempatkan tiap huruf bergantian ke rel 1..k..1
     (memantul naik-turun) -> pola zig-zag.
  3. Cipherteks = gabungan isi rel 1, rel 2, ..., rel k.

Contoh (slide): k=3
    C . . A . . A . E . I .     rel 1
    . T . . A . A . . R . P     rel 2  (dst.)
    . . R . . O . . . P . Y     rel 3
"""

def rail_fence_encrypt(plainteks: str, k: int) -> str:
    teks = "".join(ch for ch in plainteks.upper() if ch.isalpha())
    rails = [[] for _ in range(k)]
    rail = 0
    arah = 1                                  # 1 = turun, -1 = naik
    for ch in teks:
        rails[rail].append(ch)
        if k > 1:                             # pantul bila k >= 2
            if rail == 0:
                arah = 1
            elif rail == k - 1:
                arah = -1
            rail += arah
    return "".join("".join(r) for r in rails)


def rail_fence_decrypt(cipherteks: str, k: int) -> str:
    teks = "".join(ch for ch in cipherteks.upper() if ch.isalpha())
    n = len(teks)

    # 1) tandai pola zig-zag: posisi mana yang terisi per rel
    pola = []
    rail, arah = 0, 1
    for _ in range(n):
        pola.append(rail)
        if k > 1:
            if rail == 0:
                arah = 1
            elif rail == k - 1:
                arah = -1
            rail += arah

    # 2) potong cipherteks per rel sesuai jumlah marka
    rails = []
    idx = 0
    for r in range(k):
        jumlah = pola.count(r)
        rails.append(list(teks[idx: idx + jumlah]))
        idx += jumlah

    # 3) baca ulang mengikuti pola untuk merekonstruksi plainteks
    pointer = [0] * k
    plainteks = ""
    for r in pola:
        plainteks += rails[r][pointer[r]]
        pointer[r] += 1
    return plainteks


def tampilkan_zigzag(plainteks: str, k: int) -> None:
    """Menampilkan visual penulisan zig-zag (sesuai ilustrasi slide)."""
    teks = "".join(ch for ch in plainteks.upper() if ch.isalpha())
    grid = [["."] * len(teks) for _ in range(k)]
    rail, arah = 0, 1
    for i, ch in enumerate(teks):
        grid[rail][i] = ch
        if k > 1:
            if rail == 0:
                arah = 1
            elif rail == k - 1:
                arah = -1
            rail += arah
    print("\nVisual zig-zag:")
    for row in grid:
        print("  " + " ".join(row))


def main():
    print("=" * 55)
    print("   RAIL FENCE TRANSPOSITION CIPHER (kunci: jumlah rail)")
    print("=" * 55)
    while True:
        print("\nMenu:\n1. Enkripsi\n2. Dekripsi\n3. Keluar")
        pilihan = input("Pilih menu (1-3): ").strip()
        if pilihan == "1":
            pesan = input("Ketikkan pesan          : ")
            k = int(input("Jumlah rail k (>=2)     : "))
            tampilkan_zigzag(pesan, k)
            print(f"Cipherteks              : {rail_fence_encrypt(pesan, k)}")
        elif pilihan == "2":
            pesan = input("Ketikkan cipherteks     : ")
            k = int(input("Jumlah rail k (>=2)     : "))
            print(f"Plainteks               : {rail_fence_decrypt(pesan, k)}")
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


# Contoh pengujian:
# plainteks "TEKNIKINFORMATIKA", k = 3
if __name__ == "__main__":
    contoh = "TEKNIKINFORMATIKA"
    k = 3
    c = rail_fence_encrypt(contoh, k)
    print(f"[TEST] Plainteks : {contoh}")
    print(f"[TEST] Rail (k)  : {k}")
    tampilkan_zigzag(contoh, k)
    print(f"[TEST] Cipherteks: {c}")
    assert rail_fence_decrypt(c, k) == contoh, "Dekripsi gagal!"
    print(f"[TEST] Dekripsi  : {rail_fence_decrypt(c, k)} (OK)\n")
    main()
