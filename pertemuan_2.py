print("----- PERCOBAAN -----")
# TIPE DATA
# string = karakter
# integer = bilangan bulat
# float / double = bilangan desimal
# boolean = True dan False

# VARIABEL (menampilkan nilai)
# nilai_x = 10 #tidak boleh spasi
# juta10 = 10000000 #tidak diawali angka
# Nilai_x = 8 #jangan diawali kapital

a = 10
nilai_x = 5
juta10 = 1000

print("Nilai a = ", a)
print("Nilai x = ", nilai_x)
print("Harga = ", juta10)

a = 10
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

print("PROGRAM 2.3 MENGENAL TIPE DATA")
# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang tidak ada komanya (INTEGER)
data_integer = 1
print("data : ", data_integer)
print("- bertipe ", type(data_integer))

# tipe data: Angka dengan koma (FLOAT)
data_float = 1.5
print("data : ", data_float)
print("- bertipe ", type(data_float))

# tipe data: kumpulan karakter (STRING)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe ", type(data_string))

# tipe data: biner true/false (BOOLEAN)
data_bool = True
print("data : ", data_bool)
print("- bertipe ", type(data_bool))

print("\n\nPROGRAM 2.4 KONVERSI TIPE DATA")
# Casting: merubah tipe data ke tipe data lain

print("\nINTEGER ke tipe data lain")
data_int = 9
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai integer = 0

print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

print("\nFLOAT ke tipe data lain")
data_float = 9.2
data_int = int(data_float) # float ke integer
data_str = str(data_float) # float ke string
data_bool = bool(data_float) # flaot ke boolean

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))

print("\nSTRING ke tipe data lain")
data_str = "10"
data_int = int(data_str) # string ke integer
data_float = float(data_str) # string ke float
data_bool = bool(data_str) # string ke boolean

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_bool, ", type = ", type(data_bool))


print("\n\nPROGRAM 2.5 MENGAMBIL INPUT DATA DARI USER")
# data yang dimasukkan pasti string
data = input("Masukan data: ")
print("data ",data,", type =" , type(data))

# jika ingin mengambil input data integer, maka harus dikonversi ke integer
angka = int(input("Masukan angka: "))
print("data ",angka,", type =" , type(angka))

print("\n----- TUGAS -----\n")
print("1. Menyimpan Data ke dalam Variabel")
nama = "Arsyi Nisa Almatina" # Menyimpan nama (string)
umur = 18 # Menyimpan umur (integer)
berat = 38.5 # Menyimpan berat badan (float)

print("Nama  :", nama)
print("Umur  :", umur, "tahun")
print("Berat :", berat, "kg")

print("\n2. Mengubah Tipe Data")
# Menyimpan angka ke dalam variabel
angka_str = "123"
angka_float = 45.67
angka_int = 89
# Mengubah tipe data
d1 = int(angka_str) # Dari string ke integer
d2 = int(angka_float) # Dari float ke integer
d3 = float(angka_int) # Dari integer ke float
d4 = str(angka_int) # Dari integer ke string
# Menampilkan hasil konversi data
print("data = ", d1, "type = ", type(d1))
print("data = ", d2, "type = ", type(d2))
print("data = ", d3, "type = ", type(d3))
print("data = ", d4, "type = ", type(d4))

print("\n3. Membuat Program Meminta Input Data dari User")
nama = input("Masukkan Nama Anda: ") # Meminta input nama (string)
usia = int(input("Masukkan Usia Anda: ")) # Meminta input usia (integer)
tinggi = float(input("Masukkan Tinggi Badan Anda: ")) # Meminta input tinggi badan (float)
print("\nData Diri Anda")
print("Nama         : ", nama)
print("Usia         : ", usia, "tahun")
print("Tinggi Badan : ", tinggi, "cm")
