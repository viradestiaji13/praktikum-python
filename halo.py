# halo.py - program Python pertama
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

print(Fore.CYAN + "=== Program Praktikum Python ===")

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")
print(Fore.YELLOW + "Semoga sukses!")

tahun_sekarang = datetime.now().year

try:
    tahun_lahir = int(input("Masukkan tahun lahir: "))

    if tahun_lahir <= 0 or tahun_lahir > tahun_sekarang:
        print(Fore.RED + "Tahun lahir tidak valid.")
    else:
        umur = tahun_sekarang - tahun_lahir
        print(Fore.GREEN + f"Perkiraan umur Anda: {umur} tahun.")

except ValueError:
    print(Fore.RED + "Input salah! Masukkan tahun dalam bentuk angka.")