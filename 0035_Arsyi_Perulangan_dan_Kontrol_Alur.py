# print("PERCOBAAN")
# print("\nProgram 5.1 For")

# # Perulangan (loop)
# angka = 1 # tidak efisien karena harus copy 1 1
# print(angka)
# angka = angka + 1
# print(angka)
# angka = angka + 1
# print(angka)

# # for kondisi:
# #   aksi

# # dengan list
angka2 = [0,1,2,3,4] # ini adalah list
print(angka2)
for i in angka2: # i itu inisialisasi
    print(f"i sekarang -> {i}") # print(f) -> kombinasi text dan variabel
print("akhir dari program\n")

# dengan range 
angka3 = range(5) # mencetak index yaitu mulai dari 0
for i in angka3:
    print(f"i sekarang -> {i}")
print("akhir dari program")

angka4 = range(1,10) # mencetak dari rentang 1-9
for i in angka4:
    print(f"i sekarang -> {i}")
    print("saya keren")
print("akhir dari program")

# # menggunakan string
# data_str = "haii maniss"
# for huruf in data_str:
#     print(huruf)
# print("akhir dari program")

# print("\nProgram 5.2 While Loop")
# # while kondisi
# #   aksi ini
# #   aksi itu
# print("===contoh 1===\n")
# angka = 10
# while angka > 5:
#     print("ipin lari ipin!!!")

# print("===contoh 2===\n")
# angka = 0
# print(f"angka sekarang -> {angka}")
# while angka < 5:
#     angka += 1 # angka = angka + 1
#     print(f"angka sekarang -> {angka}")
#     print("ipin lari ipin !!!")
# print("program berakhir, ipin sudah jauh")

# print("\nProgram 5.3 Continue and Pass")
# # continue, pass, break

# # pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 5:
    angka = angka + 1
    if(angka == 3):
        pass # ini tidak dieksekusi
    print(angka)  

# continue 
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang -> {angka}") # aksi 1
    if(angka == 3):
        print("nice")
        continue # akan membuat loop meloncat ke step selanjutnya (melompati 1 step)
    print("whasssup") # aksi 2
print("Finish")

print("\Program 5.4 Break")
angka = 0
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka = angka + 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if(angka == 3):
        print("nice")
        break 
    print("whasssup") # aksi 2
print("cukup")


# print("\nProgram 5.5 Latihan Perulangan")


# # latihan membuat segitiga
# # 1. Menggunakan for
sisi = 4
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1

# 2. Menggunakan while
sisi = 4
count = 1

while True:
    print("*" * count)
    count += 1

    if count > sisi :
        break

sisi = 10
count = 1

for i in range(sisi):
    print("1" * count)
    count += 1


# print("\----LATIHAN---\n")
# # 1. Buat program yang menampilkan bilangan ganjil dan genap dari sampai 50 menggunakan perulangan!
print("\nDengan For")
angka = range(1,51)
for i in angka:
    if(i % 2 == 0):
        print(f"{i} adalah bilangan genap")
    else:
        print(f"  {i} adalah bilangan ganjil")
print("----akhir dari program---\n")

print("\nDengan while")
angka = 0
while angka <= 49:
    angka += 1
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"  {angka} adalah bilangan ganjil")
print("---akhir dari program---\n")

# 2. Buat program yang menampilkan semua bilanagn prima antara 1 sampai 100 menggunakan perulanagn
print("\n---mulai---")

for a in range(2,101): 
    prima = True
    for b in range(2,a): 
        if a % b == 0:
            prima = False
            break
    if prima:
        print(f"{a} adalah bilangan prima")
print("---akhir dari program---")
    

