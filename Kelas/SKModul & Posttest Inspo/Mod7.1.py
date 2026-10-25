# #1. hitung nilai akhir = nilai tugas 20%, uts 30%, dan uas 50%.

# def hitung_nilaiakhir(tugas,uts,uas):
#     nilaiakhir = (int(tugas)*20/100) + (int(uts)*30/100) + (int(uas)*50/100)
#     return nilaiakhir

# while True:
#     tugas = input("Masukkan nilai tugas.\n> ")
#     uts = input("Masukkan nilai uts.\n> ")
#     uas = input("Masukkan nilai uas.\n> ")
    
#     nilaiakhir = hitung_nilaiakhir(tugas,uts,uas)
#     print(f"Nilai akhir = {nilaiakhir}")


# # 2. Tugas harian: tunjukkan daftar & tampilkam
# tugas = []

# def show_tugas():
#     print("")
#     if not tugas:
#         print("Tugas kosong!")
#     else:
#         for i, item in enumerate(tugas,start=1):
#             print(f"{i}. {item}")

# def add_tugas():
#     baru = input("\nMasukkan tugas baru.\n> ")
#     tugas.append(baru)

# while True:
#     show_tugas()
#     add_tugas()

buku = []
def menu():
    print("""
    1. Tampilkan
    2. Tambahkan
    3. Edit
    4. Logout
""")

def tampilkan():
    if not buku:
        return
    for i, judul in enumerate(buku,start=1):
        print(f"{i}. {judul}")

def buat():
    baru = input('Masukkan judul buku baru: ')
    buku.append(baru)

def edit():
    tampilkan()
    pilihan = input("masukkan nomor buku yg ingin diedit: ")
    judul_baru = input("masukkan judul baru: ")
    buku[int(pilihan)-1] = judul_baru

while True:
    menu()
    opsi = input('Masukkan opsi: ')
    if opsi == '1':
        tampilkan()
    elif opsi == '2':
        buat()
    elif opsi == '3':
        edit()
    elif opsi == '4':
        break
    else:
        print('input tidak valid')