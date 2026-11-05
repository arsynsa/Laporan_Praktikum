print("PERCOBAAN\n")

print("Program 9.1 List")
# --- LIST ---

# Kumpulan data numbers
data_angka = [4,1,8,7]
print(data_angka)

# Kumpulan data string
data_string = ["arsyi","nisa","alma"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1,"topokki",2,"ramen","nisa",True,"nana",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0,10)]
print(list_for)

# membuat list pakai for if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 != 0 ]
print(list_for_if)

print("\n<-------------------------------------------->")

print("\nProgram 9.2 Manipulasi List")
## --- Operasi LIST ---

# index 0(-3)   1(-2)   2(-1)
data = ["Arsyi","Nisa","Alma"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list
# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

# data.insert(posisi,item)
data.insert(1,"Nana")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Rara")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["Jaemin","Jaehyun","Jeno"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi lisa
data[2] = "lisa"
print(f"data rubah = \n{data}")

# menghapus data
data.remove("Arsyi")
print(f"data hapus = \n{data}")

# menghapus data paling belakang
data.pop()
print(f"data terakhir = \n{data}")

print("\n<-------------------------------------------->")

print("\nProgram 9.3 Operasi List")
## --- Operasi List ---

# index 0(-3)   1(-2)   3(-1)
data_angka = [4,1,2,0,0,8,1,8,2,6,1,9]
print(f"data angka = \n{data_angka}")

# count data
jumlah_data_1 = data_angka.count(1)
jumlah_data_8 = data_angka.count(8)
print(f"jumlah angka 1 = {jumlah_data_1}")
print(f"jumlah angka 8 = {jumlah_data_8}")

# ambil posisi data
data = ["Keonho","Juhoon","Martin","James"]
print(f"data = {data}")

index_Juhoon = data.index("Juhoon")
index_Martin = data.index("Martin")

print(f"index si Juhoon = {index_Juhoon}")
print(f"index si Martin = {index_Martin}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

print("\n<-------------------------------------------->")

print("\nProgram 9.4 Nested List")
## --- Nested List ---

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 5,6]
print(f"list 2D = {list_2D}")

# contoh penggunaan
peserta_0 = ["Kenneth", 27, "Laki-laki"]
peserta_1 = ["Argantara", 7, "Laki-laki"]
peserta_2 = ["Amara", 55, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t : {peserta[0]}")
    print(f"Umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")

print("<-------------------------------------------->")

print("\nLATIHAN\n")

print("Nomor 1")
kendaraan = ['motor','mobil','sepeda','bus']
print(f"data awal = {kendaraan}")

# a. menambahkan 'truk' di akhir list
kendaraan.append('truk')
print(f"data ditambah = {kendaraan}")

# b. menyisipkan becak pada index ke-1
kendaraan.insert(1,'becak')
print(f"data disisipkan = {kendaraan}")

# c. menghapus data terakhir
kendaraan.pop()
print(f"data hapus = {kendaraan}")

# d. mengubah elemen 'sepeda' menjadi 'skuter'
kendaraan[3] = 'skuter'
print(f"data rubah = {kendaraan}")

# e. menampilkan informasi jumlah total data di dalam list
jumlah_data = len(kendaraan)
print(f"jumlah data = {jumlah_data}")

print("\nNomor 2")
skor_ujian = [75,80,90,75,85,100,65]
print(f"data awal = {skor_ujian}")

# a. indeks skor 100 berada
index_100 = skor_ujian.index(100)
print(f"index si 100 = {index_100}")

# b. banyak siswa yang mendapat skor 75
jumlah_skor_75 = skor_ujian.count(75)
print(f"jumlah siswa skor 75 = {jumlah_skor_75}")

# c. urutan dari skor terkecil hingga terbesar
skor_ujian.sort()
print(f"data sort = {skor_ujian}")

# d. membalikkan urutan list dari terbesar ke terkecil
skor_ujian.reverse()
print(f"data di reverse = {skor_ujian}")

print("\nNomor 3")
menu_utama = ['Nasi Goreng', 'Mie Ayam']
menu_tambahan = ['Kerupuk', 'Es Teh']
menu_utama.extend(menu_tambahan)
print(f"menu gabungan = \n{menu_utama}")

print("\nNomor 4")
data_barang = [['Buku', 5000], ['Pensil', 2000], ['Penggaris', 3000]]
# menampilkan harga pensil
harga_pensil = data_barang[1][1]
print(f"harga pensil = {harga_pensil}\n")
# menampilkan output barang
for barang in data_barang:
    print(f"Nama\t : {barang[0]}")
    print(f"Harga\t : {barang[1]}\n")
