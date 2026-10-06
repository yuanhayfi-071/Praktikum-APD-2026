import random

logged_in = False

experience = 0
day = 1
gold = 50
player_rank = 1

inventory = [{"nama":"Umpan","jumlah":5}]
aquarium = []
aqu_space = 10
desk = []
desk_space = 3

special = [
    {"name":"Penyu", "atribut":"", "harga":10},
    {"name":"Kepiting", "atribut":"", "harga":5},
    {"name":"Kuda Laut", "atribut":"", "harga":10},
    {"name":"Piranha", "atribut":"", "harga":25}, #kalau ada piranha di aquarium, ikan lain mati semua
    {"name":"Ketimun Laut", "atribut":"","harga":50}
]
normal = [
    {"name":"Ikan Kerapu", "atribut":"", "harga":2},
    {"name":"Ikan Lele", "atribut":"", "harga":2},
    {"name":"Ikan Kakap", "atribut":"", "harga":2}
]
# misc = ["gold pancing", "sampah"]

pool = special+normal 
# +misc
pot_atribut = ["SSR","SR","R"]

item = [
    {"name":"Telur Acak", "deskripsi":"Tidak ada yang tahu ini telur apa."},
    {"name":"Jala","deskripsi":"Digunakan untuk menangkap biota, kadang telur, kadang sampah."}
    ]

def login():
   global logged_in
   player_name = input("Namaku adalah: ").upper()
   logged_in = True
   return player_name

def menu():
    print("\n=====MANCING.SIMULATOR=====")
    print(f"RANK [{player_rank}] | GOLD [{gold}]")
    print("Ketik [Profil] | [Mancing] | [Akuarium] | [Toko] | [Inventori]")
    pilih_menu = input("\n> ").strip().lower()
    return pilih_menu

def cek_profil():
   print(f"\n=====PROFIL {player_name}=====")
   print(f"Nama: {player_name}")
   print(f"Rank: {player_rank}")
   print(f"Gold: {gold}")
   print(f"Day: {day}")

def tampilkan_aqu():
    print(f"\n=====AKUARIUM {player_name}=====")
    if not aquarium:
       print("Akuarium anda kosong!")
       return
    else:
        aquarium.sort(key=lambda k:k["name"])
        for i, k in enumerate(aquarium, start=1):
            print(f"{i}. {k['name']} | {k['atribut']} | {k['harga']}")

    while True:
        pilih = input(f"\nKetik 'jual [index]' untuk menjual atau 'tutup'.\n> ")
        bagian = pilih.lower().split()
        if len(bagian) == 2 and bagian[0] == "jual" and bagian[1].isdigit():
            index = int(bagian[1])
            if 1 <= index <= len(aquarium):
                listing = aquarium.pop(index -1)
                jual(listing)
                return
            else:
                print("Index tidak ditemukan.")
        elif bagian[0] == "tutup":
            break
        else:
            print("Perintah tidak dikenali.")


# def beli():

def jual(item):
    global gold
    print(f"{item['name']} terjual!")
    gold += item["harga"]

# def tampilkan_toko():
#     print(f"\n=====TOKO=====")
#     print("1. Telur Acak")
#     print("2. Jala")
#     print("3. Umpan")
#     print("================")
#     pilihan = input("Ketik 'beli' atau 'jual' [nomor item]\n")

def mancing():
    print("\nMemancing...")
    tangkapan = random.choice(pool).copy()
    atribut = random.choice(pot_atribut)
    tangkapan["atribut"] = atribut
    if atribut == "SSR":
        tangkapan["harga"] += 10
    elif atribut == "SR":
        tangkapan["harga"] += 5
    else:
        tangkapan["harga"] += 2
    print(f"Mendapatkan: {tangkapan['name']} {atribut} {tangkapan['harga']}G)!")
    return tangkapan

def tambahke_aqu(tangkapan):
    while True:
        tambahkan = input(f"\nKetik 'simpan' atau 'jual' {tangkapan['name']} ke akuarium\n> ")
        if tambahkan.strip().lower() == "simpan":
            aquarium.append(tangkapan)
            print(f"{tangkapan['name']} ditambahkan!")
            break
        elif tambahkan.strip().lower() == "jual":
            jual(tangkapan)
            break
        else:
            print("Perintah tidak ditemukan!")
            
# def lihat_biota():

# def beri_makan():

# def bersihkan_aqu():

while True:
    if not logged_in:
        player_name = login()

    if logged_in:
        hasil = menu()
        if hasil == "profil":
            cek_profil()
        elif hasil == "mancing":
            tangkapan = mancing()
            tambahke_aqu(tangkapan)
        elif hasil == "akuarium":
            tampilkan_aqu()
        elif hasil == "toko":
            print("Membuka toko...")
        elif hasil == "inventori":
            print("Membuka inventori...")
            for i, barang in enumerate(inventory, start=1):
                print(f"{i}. {barang['nama']} x{barang['jumlah']}")
        else:
            print("Perintah tidak dikenal!")