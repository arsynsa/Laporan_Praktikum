print("======= PERCOBAAAN =======")

print("\nProgram 11.1 Multi Keys & Nesting Dictionary")

import datetime
mahasiswa1 = {
    'nama':'Arsyi Nisa Almatina',
    'nim':2605060035,
    'sks_lulus':144,
    'beasiswa':False,
    'lahir':datetime.datetime(2008,1,4) # tahun, bulan, tanggal
}

mahasiswa2 = {
    'nama':'Kevan Mahendra',
    'nim':2605060082,
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2007,11,27)
}

mahasiswa3 = {
    'nama':'Jenandra Alexander',
    'nim':2605060083,
    'sks_lulus':120,
    'beasiswa':True,
    'lahir':datetime.datetime(2008,3,15)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<20} {'SKS':<3} {'Beasiswa':^9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<20} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")


print("\nProgram 11.2 Latihan Dictionary Bagian 1")

import datetime
mahasiswa_template = {
    'nama':'nama',
    'nim':0000000000,
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

print(f"{'SELAMAT DATANG':^60}")
print(f"{'DATA MAHASISWA':^60}")
print("-"*60)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)

mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
tahun_lahir = int(input("Tahun Lahir (YYYY): "))
bulan_lahir = int(input("Bulan Lahir (1-12): "))
tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
print(mahasiswa)

print("\nProgram 11.3 Latihan Dictionary Bagian 2")

import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':0000000000,
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    # os.system("cls") # untuk windows
    # os.system("clear")
    print("-"*60)
    print(f"{'SELAMAT DATANG':^60}")
    print(f"{'DATA MAHASISWA':^60}")
    print("-"*60)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    tahun_lahir = int(input("Tahun Lahir (YYYY): "))
    bulan_lahir = int(input("Bulan Lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    # dari program sebelumnya, hilangkan beasiswa
    print(f"\n{'KEY':<6} {'Nama':^17} {'NIM':^8} {'SKS Lulus':^15} {'Tanggal Lahir':<10}")
    print('-'*65)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^15} {LAHIR:^10}")

    print("\n")
    is_done = input("Mau tambah lagi (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")

print("\n======= LATIHAN =======\n")
print("PROGRAM SISTEM MANAJEMEN PERPUSTAKAAN")

import datetime
import os
import string
import random

peminjaman_template = {
    'judul_buku':'judul_buku',
    'penulis':'penulis',
    'tahun_terbit':0,
    'tanggal_terakhir_pinjam':datetime.datetime(1111, 1, 11),
    'status':'Tersedia'
}

data_buku = {}

while True:
    os.system("cls")
    print("="*90)
    print(f"{'SELAMAT DATANG DI PERPUSTAKAAN':^90}")
    print(f"{'DATA PEMINJAMAN BUKU':^90}")
    print("="*90)

    buku = dict.fromkeys(peminjaman_template.keys())
    buku['judul_buku'] = input("Judul Buku\t\t: ")
    buku['penulis'] = input("Nama Penulis\t\t: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit\t\t: "))
    print("Tanggal Terakhir Pinjam\t: ")
    tahun = int(input("\tTahun (YYYY)\t: "))
    bulan = int(input("\tBulan (1-12)\t: "))
    tanggal = int(input("\tTanggal (1-31)\t: "))
    buku['tanggal_terakhir_pinjam'] = datetime.datetime(tahun, bulan, tanggal)
    buku['status'] = input("Status (Tersedia/Tidak)\t: ")
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))
    data_buku.update({KEY:buku})

    print(f"\n\n{'KEY':^6} | {'Judul Buku':^15} | {'Penulis':^15} | {'Tahun Terbit':^12} | {'Terakhir Pinjam':^15} | {'Status':^8}")
    print("-"*90)

    for buku in data_buku:
        KEY = buku
        JUDUL = data_buku[KEY]['judul_buku']
        PENULIS = data_buku[KEY]['penulis']
        TERBIT = data_buku[KEY]['tahun_terbit']
        PINJAM = data_buku[KEY]['tanggal_terakhir_pinjam'].strftime("%x")
        STATUS = data_buku[KEY]['status']
        
        print(f"{KEY:^6}   {JUDUL:<15}   {PENULIS:<15}   {TERBIT:^12}   {PINJAM:^15}   {STATUS:^8}")
        print("-"*90)

    print("\n")
    is_done = input("Ingin menambah peminjaman buku (y/n)? ")
    if is_done == "n":
        break
print("\nPeminjaman Anda berhasil, terima kasih telah berkunjung >ᴗ<\n")
