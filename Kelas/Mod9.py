# #set
# angka = {1,1,1,2,3,3,2+1+3}
# prima = {2,3,5,7}
# print(angka)

# #union
# print(angka.union(prima.union(angka.union(prima))))
# print(angka | prima)

# #interception(irisan)
# print(angka & prima)
# print(angka.intersection(prima))
# print(angka.intersection(prima.union(angka)))

# #difference
# print(angka.difference(prima))
# print(angka - prima)
# print(prima.difference(angka))
# print(prima - angka)

# #discard & remove
# print(prima.add(11))
# print(prima.discard(55))

# kendaraan = {
#     'Mobil': 'innova',
#     'Sepeda': 'bmx'
# }
# print(kendaraan.get('Mobil'))
# print(kendaraan.get('obil'))
# for item in kendaraan:
#     print(item)
# for item in kendaraan.values():
#     print(item)
# for item in kendaraan.items():
#     print(item)
# for key, value in kendaraan.items(): #-> items menampung key + value
#     print(f"{key} : {value}")

# kendaraan['Pesawat'] = 'boeing' #cara nambah scr lgsg
# kendaraan.update({'Kapal':'kapal laut', #cara nambah pake update (union operation)
#                   'Helikopter':'Heli'})

# kendaraan['Mobil'] = "Toyota"

# poli_umum = {"Andi", "Budi", "Citra", "Doni"}
# poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
# gabung = []

# for nama in poli_umum:
#     if nama in poli_gigi:
#         continue
#     else:
#         gabung.append(nama)
# for nama in poli_gigi:
#     gabung.append(nama)
# print(gabung)

# etalase = {
#     "6767": {"nama":"Apel","harga":50,"stok":11},
#     "1999": {"nama":"Pisang","harga":1,"stok":90000},
#     "1": {"nama":"Alpukat","harga":20090304,"stok":17}
# }
# for IDitem in etalase:
#     print(f"{IDitem} - {etalase[IDitem]['nama']} | Rp. {etalase[IDitem]['harga']} | Tersedia: {etalase[IDitem]['stok']}")

# angka = {
#     'Prima' : [2,3,4,7,11, {
#         'Ganjil' : [13,1,7]
#     }]
# }
# print(angka['Prima'][5]['Ganjil'][2])