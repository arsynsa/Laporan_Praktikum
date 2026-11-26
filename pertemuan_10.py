# def nama_fungsi(): () ---> parameter
#   badan fungsi
#   return (opsional)
# nama_fungsi() ---> memanggil fungsi

print("Program 12.1 Pengenalan Fungsi")

def love():
    print("hai manis")
    print("apa kabar?")
    print("masih ingat aku?")
love()

print("\nProgram 12.2 Fungsi dengan Argumen")
# def nama_fungsi(argumen):
#       Badan fungsi

def hello_world(nama):
    # fungsi hello world menerima
    print(f"Selamat datang di dunia {nama}")
hello_world("arsyi")

def tambah(angka_1, angka_2):
    # fungsi tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
tambah(3,4)

def say_hi(list_peserta):
    # fungsi say hi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Selamat datang {peserta}")
kumpulan_mahasiswa = ["Arsyi", "Nisa", "Alma"]
say_hi(kumpulan_mahasiswa)


print("\nProgram 12.3 Fungsi dengan Return")
# template fungsi kembalian
# def nama_fungsi(argumen):
#       badan fungsi
#       return output

def luasLingkaran(jariJari):
    phi = 3.14
    luas = 3.14 * (jariJari * jariJari)
    return luas

luas = luasLingkaran(10)
luasAkhir = luas * 2
print(luasAkhir)


# fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(4)
print(y)
print(kuadrat(9))

z = 20 - kuadrat(3)
print(z)


def fungsi_tambah(angka_1, angka_2):
    # fungsi return dengan multi input
    return angka_1 + angka_2

a = fungsi_tambah(3, 5)
print(a)


def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi

k,l,m,n = operasi_matematika(11,4)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")

print("\nProgram 12.4 Default Argumen Fungsi")
# def fungsi(argumen):
# def fungsi(argumen = nilai default):

# contoh 1
def say_hello(nama = "Keeneth"): # default nilai
    print(f"Hello {nama}")

say_hello("Kalula")
say_hello()

# contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    # fungsi dengan satu input biasa dan satu default argumen
    print(f"hai {nama}, {pesan}")

sapa_dia("Bila", "cantik")
sapa_dia("James")

# contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(3,1))
hasil = hitung_pangkat(pangkat=3, angka=4)
print(hasil)

# contoh 4
def faktorial(input_1=1, input_2=2, input_3=3, input_4=4):
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil

print(faktorial())
print(faktorial(input_3=5))

print("\n\nLATIHAN\n")

print("==== Menghitung Luas Persegi Panjang ====")
def luasPersegiPanjang(panjang, lebar):
    luas = panjang * lebar
    return luas
panjang = float(input("Panjang\t: "))
lebar = float(input("Lebar\t: "))
luas = luasPersegiPanjang(panjang, lebar)
print(f"Luas persegi panjang adalah {luas}")

print("\n=== Menghitung Volume Persegi Panjang ===")
def volumePersegiPanjang(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume
panjang = float(input("Panjang\t: "))
lebar = float(input("Lebar\t: "))
tinggi = float(input("Tinggi\t: "))
volume = volumePersegiPanjang(panjang, lebar, tinggi)
print(f"Volume persegi panjang adalah {volume}")

print("\n======= Menghitung Luas Lingkaran =======")
def luasLingkaran(jari_jari):
    phi = 3.14
    luas_lingkaran = phi * jari_jari * jari_jari
    return luas_lingkaran
jari_jari = float(input("Jari-jari lingkaran: "))
luas_lingkaran = luasLingkaran(jari_jari)
print(f"Luas lingkaran adalah {luas_lingkaran}")

print("\n======== Menghitung Volume Bola =========")
def volumeBola(jari_jari):
    phi = 3.14
    volume_bola = 4/3 * phi * (jari_jari ** 3)
    return volume_bola
jari_jari = float(input("Jari-jari bola: "))
volume_bola = volumeBola(jari_jari)
print(f"Volume bola adalah {volume_bola}")
