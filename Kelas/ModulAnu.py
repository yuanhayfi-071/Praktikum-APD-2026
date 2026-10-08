# formula1 = ["Suzuka", 30, 37.5, True, ["apel", "lemari"]]
# print(f"Memanggil index ke-1: {formula1[1]}")
# print(f"Memanggil formula sebelum append: {formula1}")
# formula1.append("Anu")
# print(f"Memanggil formula setelah append: {formula1}")
# formula1.extend(["extend satu","extend dua","extend kesekian"])
# print(f"Memanggil formula setelah extend: {formula1}")
# formula1.insert(1, "insert i ke-1")
# print(f"Memanggil formula setelah insert ke index ke-1: {formula1}")

# for index, x in enumerate(formula1, start=1):
#     print(f"{index}. tipe data {x} adalah {type(x)}")

# formula1[4] = "Celana panjang"
# print(f"Mengubah item ke-4 menjadi 'celana panjang': {formula1}")

# formula1[0:2] = ["Ani","Ana"]
# print(f"Mengubah indeks ke-0 dan sebelum indeks ke-2: {formula1}")

# del formula1[1]
# print(formula1)

# formula1.remove("Ani")
# print(formula1)

# hapus = "Celana panjang"
# formula1.remove(hapus)
# print(formula1)

# sisa = formula1.pop(0)
# print(f"{sisa} telah dihapus!")

# angka = (1,2,3, "halo",True)
# print(angka)
# ubah = list(angka)
# ubah.append("hai")
# angka = tuple(ubah)
# print(angka)

anu = "Senku", "Amamiya Ren", "Shirakumo Oboro" # ga pake tanda kurung ttp jadi tuple. itu biar standar aja
(drstone, *apayok) = anu
print(drstone)
print(apayok)