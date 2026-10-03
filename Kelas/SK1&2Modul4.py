#for loop
# batas = 10
# for i in range(batas):
#     print(i)

# nilai = [75, 60, 80, 90, 60]
# for element in nilai:
#     if element >= 70:
#         print(f"Lulus dengan nilai {element}")
#     else:
#         print(f"Tidak lulus dengan nilai {element}")

# struktur range(start, stop, step)
# for i in range(5, 0 , -1):
#     print(f"ini angka ke {i}")

# nested for
# for i in range(2): #berhenti sebelum 2, alias 0-1
#     for j in range(3): #berhenti sebelum 3, alias 0-2
#         print(f"{i} x {j} = {i}*{j}")

# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     print(f"anda berada di perulangan ke {hitung}")
#     jawab = input("ulangi lagi tidak? ")
# print(f"total perulangan: {hitung}")
# #jadi ada yang namanya input buffer, makanya yg terakhir juga dihitung perulangan

# for i in range(10):
#     if i % 2 == 0:
#         continue #buat ngeskip kode di bawah dan lanjut ke iterasi berikutnya
#     print(i)

#Sk 1
jumlah_ganjil = 0
bilangan_bulat = int(input("Masukkan bilangan: "))
for i in range(bilangan_bulat):
    if i % 2 == 0:
        jumlah_ganjil += 1
print(f"Jumlah bilangan ganjil adalah {jumlah_ganjil}")

#Sk 2
saldo = int(input("Masukkan uang saku awal: "))
while saldo != 0:
    pengeluaran = int(input("Masukkan pengeluaran: "))
    if saldo >= pengeluaran:
        saldo -= pengeluaran
        if saldo != 0:
            print(f"Sisa saldo anda: Rp.{saldo}")
    else:
        print("Saldo anda tidak mencukupi.")
        continue
print(f"Saldo habis. Sisa saldo anda Rp.{saldo}!")