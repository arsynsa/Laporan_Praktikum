print("=====PERCOBAAN=====")

print("\nProgram 4.1 Logical")
print('===NOT===') # kebalikan 
a = True
b = not a
print('data a = ',a)
print('------------ NOT')
print('data b = ',b)
# OR (akan true jika salah satu nilaiya true)
print('===OR===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)
# AND (akan bernilai true jika keduanya true)
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True 
c = a and b
print(a,'AND',b,'=',c)
# XOR (akan true jika salah satu true, namun akan false jika sama-sama true/false)
print('===XOR===')
a = False 
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True 
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

print("\nProgram 4.2 Logika dan Komparasi")
# menentukan angka kurang dari 3 dan lebih dari 10
angka = float(input("masukkan angka: "))
isKurangDari = angka < 3 # memeriksa angka kurang dari 3
print("Kurang dari 3 = ", isKurangDari)
isLebihDari = angka > 10 # memeriksa angka lebih dari 10
print("Lebih dari 10 = ", isLebihDari)
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

print("\nProgram 4.3 IF dan ELSE")
nama = input("masukkan nama Anda: ")
# program if inline
if nama == "alma" : print("Kamu hebat!!!")
# program if identation
if nama == "alma" :
    print("Kamu hebat!!!")
    print("Kamu juga keren!!!")
# Else statement
if nama == "nisa" :
    print("Hai nisa, kamu keren banget")
else:
    print("Kamu bukan nisa, tapi kamu tetap keren")

print("\nProgram 4.4 ELIF Statement")
# elif (else if) digunakan jika ada lebih dari 1 kondisi
nama = input("masukkan nama Anda: ")
if nama == "arsyi": # kondisi 1
    print("hai manis") # aksi true 1
elif nama == "ana": # kondisi 2
    print("hai cantik") # aksi true 2
elif nama == "ara": # kondisi 3
    print("hai sis") # aksi true 3
else:
    print("hai, salam kenal") # aksi false


print("\nLATIHAN")
# Membuat program meminta input usia dari user lalu menentukan kategori usia tersebut berdasarkan kriteria berikut:
# 0-12 tahun : Anak-anak
# 13-17 tahun : Remaja
# 18-59 tahun : Dewasa
# 60 tahun ke atas : Lansia

usia = int(input("masukkan usia Anda: ")) # meminta data usia dari user
if usia >= 0 and usia <= 12 : # kondisi pertama
    print("Anda termasuk kategori Anak-anak")
elif usia >= 13 and usia <= 17 : # kondisi kedua
    print("Anda termasuk kategori Remaja")
elif usia >= 18 and usia <= 59 : # kondisi ketiga
    print("Anda termasuk kategori Dewasa")
elif usia >= 60 : # kondisi keempat
    print("Anda termasuk kategori Lansia")
else:
    print("usia tidak valid")

print("---akhir dari program---")
