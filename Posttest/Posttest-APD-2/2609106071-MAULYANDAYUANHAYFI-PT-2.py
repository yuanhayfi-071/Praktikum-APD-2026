#masukkan nilai terlebih dahulu
harga_komponen = [120000, 135000, 150000, 175000, 200000, 220000]
biaya_admin = 15000
total_biaya = 0 + 15000

#menghitung total biaya & rata-rata
for index in harga_komponen:
    total_biaya += index
rata_rata = total_biaya/len(harga_komponen)

#melakukan sesuatu dengan nim
nim = 71
boolean = nim != rata_rata

#print semua variabel yang perlu di-print
print("\n")
for index, harga in enumerate(harga_komponen):
    print(f"harga komponen ke-{index +1}: Rp.{harga}")
print(f"\nbiaya admin: Rp.{biaya_admin}")
print(f"total biaya: Rp.{total_biaya}")
print(f"rata-rata: {rata_rata}")
print(f"nim: {nim}")
print(f"boolean: {boolean}")

#print total biaya dalam pound sterling
kurs_gbp = 23.860
harga_dalam_gbp = total_biaya/kurs_gbp
print(f"\nbiaya dalam GBP: £{harga_dalam_gbp}")

#print 1-4 dg. slice index negatif
print(f"\nharga komponen ke-4 hingga ke-1: {harga_komponen[3::-1]}")