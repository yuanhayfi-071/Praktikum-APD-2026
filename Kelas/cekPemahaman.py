import os

mahasiswa = {
    'nama':"Maulyanda Yuan Hayfi",
    'nim':2609106071,
    'prodi':"Informatika",
    'semester':1
}

def clear_terminal():
    os.system("cls" if os.name == 'nt' else "clear")

def tampilkan():
    clear_terminal()
    for i, (key, value) in enumerate(mahasiswa.items(), start=1):
        print(f"{i}. {key} : {value}")

def ubah():
    pilih = input("Ketik nama field untuk diubah.\n> ")
    for i in mahasiswa:
        if i == pilih:
            field = pilih
            break
    if not field:
        print("Field tidak ditemukan.")
        return

    new_value = input(f"Masukkan nilai baru untuk {field} mahasiswa.\n> ")
    mahasiswa.update({field:new_value})
    print(f"Nilai berhasil diubah!")

def tambah():
    clear_terminal()
    new_value = input("Masukkan nama field baru.\n> ")
    mahasiswa.update({new_value:None})

while True:
    pilih = input("PILIH AKSI 1. Tampilkan, 2. Ubah, 3. Tambah \n> ")
    if pilih == "1":
        tampilkan()
    elif pilih == "2":
        ubah()
    elif pilih == "3":
        tambah()
    else:
        print("Opsi tidak ditemukan")
