"""
=====================================================
 Caesar Cipher - Cipher Substitusi Abjad-Tunggal
 (Monoalphabetic Substitution Cipher)
 Materi: 03 - Ragam Cipher Klasik Bagian 1
 Ref     : Dr. Ir. Rinaldi Munir (STEI ITB, 2025)
=====================================================
Prinsip : Setiap huruf plainteks digeser sejauh k
          posisi ke kanan dalam urutan alfabet.

Formulasi matematika (p, c dalam [0..25], A=0..Z=25):
    Enkripsi : c = E(p) = (p + k) mod 26
    Dekripsi : p = D(c) = (c - k) mod 26

Catatan kriptanalisis (slide hal. 21):
Caesar Cipher mudah dipecahkan dengan exhaustive key
search (brute force) karena jumlah kunci hanya 26.
ROT13 adalah kasus khusus dengan k = 13, di mana
enkripsi = dekripsi (ROT13(ROT13(x)) = x).
"""

def caesar_encrypt(plainteks: str, k: int) -> str:
    """Enkripsi plainteks dengan Caesar Cipher.
    Hanya huruf alfabet yang diproses; karakter lain
    (spasi, angka, tanda baca) dibiarkan apa adanya."""
    cipherteks = ""
    for char in plainteks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            c = (ord(char) - start + k) % 26   # geser sejauh k
            cipherteks += chr(c + start)       # kembalikan ke huruf semula
        else:
            cipherteks += char                 # non-alfabet tidak dienkripsi
    return cipherteks


def caesar_decrypt(cipherteks: str, k: int) -> str:
    """Dekripsi cipherteks Caesar Cipher (geser berlawanan arah)."""
    return caesar_encrypt(cipherteks, -k)


def brute_force(cipherteks: str) -> None:
    """Exhaustive key search: coba semua kunci 0..25.
    Teknik pemecahan Caesar Cipher sesuai slide hal. 21-24."""
    print(f"{'k':>3} | Hasil Dekripsi")
    print("-" * 40)
    for k in range(26):
        print(f"{k:>3} | {caesar_decrypt(cipherteks, k)}")


def main():
    print("=" * 50)
    print("   CAESAR CIPHER (kunci k = 0..25)")
    print("=" * 50)
    print("Menu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Brute Force (kriptanalisis, semua kunci)")
    print("4. Keluar")
    while True:
        pilihan = input("\nPilih menu (1-4): ").strip()
        if pilihan == "1":
            pesan = input("Ketikkan pesan  : ")
            k = int(input("Masukkan kunci k (0-25): ")) % 26
            cipher = caesar_encrypt(pesan, k)
            print(f"Cipherteks      : {cipher}")
        elif pilihan == "2":
            pesan = input("Ketikkan cipherteks: ")
            k = int(input("Masukkan kunci k (0-25): ")) % 26
            print(f"Plainteks       : {caesar_decrypt(pesan, k)}")
        elif pilihan == "3":
            pesan = input("Ketikkan cipherteks: ")
            brute_force(pesan)
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


# Contoh pengujian (dapat dijalankan langsung):
# plainteks "KRIPTOGRAFI", k = 3 -> cipherteks "NULSWRJUDIL"
if __name__ == "__main__":
    contoh = "KRIPTOGRAFI"
    k = 3
    c = caesar_encrypt(contoh, k)
    print(f"[TEST] Plainteks : {contoh}")
    print(f"[TEST] Kunci     : {k}")
    print(f"[TEST] Cipherteks: {c}")
    assert c == "NULSWRJUDIL", "Hasil enkripsi tidak sesuai!"
    assert caesar_decrypt(c, k) == contoh, "Dekripsi gagal!"
    print("[TEST] Dekripsi  :", caesar_decrypt(c, k), "(OK)\n")
    main()
