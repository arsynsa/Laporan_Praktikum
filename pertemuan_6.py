print("--- Nested IF ---\n") # if bersarang
# if kondisi_utama:
    # if kondisi_lanjutan:
        # Aksi jika kedua kondisi bernilai True
    # else:
        # Aksi jika kondisi_utama True, tetapi kondisi_lanjutan False
# else:
    # Aksi jika kondisi_utama False

status_kartu = "aktif" # kadaluarsa
saldo = 500000
nominal_tarik = 100000

if status_kartu == "aktif":
    if nominal_tarik <= saldo:
        if nominal_tarik >= 50000:
            sisa_saldo = saldo - nominal_tarik
            print(f"Penarikan berhasil: Rp{nominal_tarik}")
            print(f"Sisa saldo: Rp{sisa_saldo}")
        else:
            print("penarikan minimal Rp50,000.")
    else:
        print("saldo anda tidak mencukupi")
else:
    print("kartu anda tidak aktif")

print("\n--- Nested While ---\n")
print("contoh 1")
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print("jaehyun")
        j += 1
    print("\n") # Mencetak baris baru (\n) saat inner loop selesai
    i += 1

print("\ncontoh 2")
i = 1
N = 1
while i <=2:
    j = 1
    while j <= 3:
        print(N)
        N = N + 2
        j += 1
    i +=1

print("\n--- Nested For ---\n")
for i in range(1,3):        # Outer loop (baris 1 s.d 2)
    for j in range(1,4):    # Inner loop (kolom 1 s.d 3)
        print(f"[{i},{j}]", end=" ")
    print() # Memberi jarak 1 baris

print("\n--- For in While ---\n")
# for_in_while.py
sesi = 1
while sesi <= 3:
    print(f"Sesi ke-{sesi}")
    # Inner for: mencetak nomor antrean pada sesi tersebut
    for antrean in range(1,4): # 3 nomor antrean yang dapat diambil
        print(f"    Melayani pasien nomor: {antrean}")
    sesi +=1
    print("---") # memberi jarak antara sesi 1 dan 2