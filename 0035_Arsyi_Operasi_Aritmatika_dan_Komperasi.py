print("==========PERCOBAAN==========")

print("\nProgram 3.1 Menampilkan output dari operasi aritmatika sederhana")
# operasi aritmatika
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)
# operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)
# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)
# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)
# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)
# operasi modulus % (sisa pembagian)
hasil = a % b
print(a,'%',b,'=',hasil)
# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

print("\n\nProgram 3.2 Konversi celcius ke satuan lain")
# latihan konversi satuan temperature
# program konversi celcius ke satuan lain
print("\nProgram Konversi Temperatur\n")
celcius = float(input('Masukkan suhu dalam celcius: '))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalaha", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius + 32)
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "Kelvin")


print("\n\nProgram 3.3 Operasi komperasi")
# operasi komperasi 
# setiap hasil dari operasi komperasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not
a = 4
b = 2
# lebih besar dari (>)
print("=============== lebih besar dari (>)")
hasil = a > b
print(a,'>',b,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari (<)
print("=============== kurang dari (<)")
hasil = a < b
print(a,'<',b,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan (>=)
print("=============== lebih dari sama dengan (>=)")
hasil = a >= b
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan (<=)
print("=============== kurang dari sama dengan (<=)")
hasil = a <= b
print(a,'<=',b,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print("=============== sama dengan (==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print("=============== tidak sama dengan (!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

print("=============== is dan is not")
# 'is' sebagai komparasi obj identity (bukan literal)
x = 5
y = 5
hasil = x is y
print('x is y =',hasil)

# 'is not' sebagai komparasi obj identity (bukan literal)
x = 5 
y = 6
hasil = x is not y
print('x is not y =',hasil)

print("\n==========LATIHAN==========\n")
print("a. Hitunglah luas, volume, dan keliling dari bangunan tersebut!")

p = 12
l = 5
t = 8

luas = 2 * ((p*l)+(p*t)+(l*t))
volume = p*l*t
keliling = 4 * (p+l+t)

print("- Luas bangunan adalah", luas, "cm²")
print("- Volume bangunan adalah", volume, "cm³")
print("- Keliling bangunan adalah", keliling, "cm")

print("\nb. Apakah luas bangunan tersebut lebih luas dari 50?")
hasil = luas > 50
print(luas,'>',50,'=',hasil)

print("\nc. Apakah volume tersebut bernilai 480?")
hasil = volume == 480
print(volume,'==',480,'=',hasil)
