print("--------PERCOBAAN--------")

print("\nProgram 10.1 Tuples dan sets")
# LIST : menggunakan kurung siku
data_list = [10,2,4,3,2]
print(data_list)

# TUPLES : menggunakan kurung biasa
data_tuples = (1,2,8,9)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append[1]

# SETS (himpunan) : menggunakan kurung kurawal
data_sets = {8,1,3,2,7,6,8}
print(data_sets)
# print(data_sets[0])

print("\nProgram 10.2 Dictionary")
# LIST -> array, mengakses dengan menggunakan index
# data_list = ["Jaehyun", 29, "Laki-laki", 180]
print(data_list[0])

# DICTIONARY (dict) -> associative array, mengakses dengan menggunakan key
# identifier -> key

data_list = ["Jaehyun", 29, "Laki-laki", 180]
member_nct = {
    "key" : "value", # key harus ditulis dalam tanda petik, meskipun angka
    "Nama" : "Jaehyun",
    "Umur" : 29,
    "JK" : "Laki-laki",
    "TB" : 180,
    "List" : data_list
}
print(member_nct["Nama"]) # untuk menampilkan penulisan key juga harus menggunakan tanda petik
print(member_nct["Umur"])
print(member_nct["List"])

print("\nProgram 10.3 Operasi Dictionary")
data_mahasiswi = {
    "Nama" : "Evelyn",
    "Usia" : 18,
    "Prodi" : "Sastra Inggris"
}

# panjang dictionary
LENDICT = len(data_mahasiswi)
print(f"panjang dictonary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "Nama"
CHECKKEY = KEY in data_mahasiswi
print(f"apakah {KEY} ada di data_mahasiswi: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_mahasiswi["Nama"])
print(data_mahasiswi.get("Nama"))
print(data_mahasiswi.get("Alamat", "data tidak ditemukan")) # check key dengan message

# mengupdate data
data_mahasiswi["Prodi"] = "Teknologi Informasi"
print(data_mahasiswi)

data_mahasiswi.update({"Usia" : 19})
print(data_mahasiswi)
data_mahasiswi.update({"Hobi" : "membaca"}) # akan di tambah jika tidak ada
print(data_mahasiswi)

# menghapus data
del data_mahasiswi["Hobi"]
print(data_mahasiswi)

print("\n10.4 Looping Dictionary")
karyawan = {
    "Nama" : "Ara",
    "Jabatan" : "IT Support",
    "Gaji" : 5000000
}

# looping first try (yang keluar hanya key)
for i in karyawan:
    print(i)

# operator untuk mengambil item (nilai)

# menampilkan key saja
keys = karyawan.keys()
print(keys)

for key in karyawan.keys():
    print(karyawan.get(key))

# menampilkan value saja
values = karyawan.values()
print(values)

for value in karyawan.values():
    print(value)

# menampilkan key dan value sekaligus
items = karyawan.items()
print(items)

for item in karyawan.items():
    print(item)

for key, value in karyawan.items(): 
    print(f"{key}\t: {value}")


print("\n===== LATIHAN =====\n")

print("Nomor 1 - Tuple")
# a. Membuat Tuple
mahasiswa = ("Arsyi Nisa Almatina", 2605060035, "Teknologi Informasi")
# b. Menampilkan data NIM dan Prodi
print(mahasiswa[1])
print(mahasiswa[2])
# c. Menjalankan kode mahasiswa[2] = "Teknologi Informasi"
# mahasiswa[2] = "Teknologi Informasi"
# print(mahasiswa)
# d. Membuat Set 
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

print("\nNomor 2 - Manipulasi Dictionary")
# a. Membuat dictionary
data_mahasiswa = {
    "nim" : "240101",
    "nama" : "Budi Santoso",
    "prodi" : "Teknologi Informasi"
}
# b. Mengubah nilai "prodi" menjadi "Sastra Mesin" dan menambahkan key baru "angkatan" dengan nilai 2026
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa.update({"angkatan" : 2026})
print(data_mahasiswa)
# c. Menghapus data "nim"
del data_mahasiswa["nim"]
print(f"Data akhir: \n{data_mahasiswa}")

print("\nNomor 3 - Perulanangan pada Dictionary")
# Membuat dictionary
keranjang = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}
# Menampilkan buah, harga, dan total belanja
total_belanja = 0
for buah,harga in keranjang.items():
    total_belanja += harga
    print(f"Harga {buah}\t: Rp {harga}")
print(f"Total belanja\t: Rp {total_belanja}")
