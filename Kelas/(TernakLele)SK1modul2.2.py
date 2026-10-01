# Seorang karyawan akan menerima gaji dari perusahaan ternak lele tempat ia
# bekerja dengan ketentuan sebagai berikut:
# ● Gaji pokok = 2.000.000
# ● Bonus total panen = Rp. 5.000/Kilogram
# ● Pph (Pajak Penghasilan) = 10% dari gaji pokok + bonus
# ● Total Gaji = (Gaji pokok + bonus) - Pph
# Buatkan program yang dapat menghitung total gaji karyawan tersebut dan
# tampilkan hasilnya!

gaji_pokok = 2000000
data_panen = [{"nama":"MANUSIA PALING SEMPURNA","total setoran":999}]

def menghitung_gaji():
    nama_karyawan = input("\nMasukkan nama anda: ").upper()    
    while True:
        panen_mentah = (input("Masukkan total panen anda (kg) atau ketik 'keluar': "))
        if panen_mentah.lower().strip() == "keluar":
            return
        try: 
            panen_int = int(panen_mentah)
            bonus = 5000 * panen_int
            pph = (gaji_pokok + bonus) * 0.1
            gaji_total = (gaji_pokok + bonus) - pph

            print("\nNama: " + nama_karyawan)
            print(f"Jumlah panen: {panen_int} kg")
            print(f"Gaji anda dipotong pajak: Rp. {gaji_total}")
            return nama_karyawan, panen_int
        except ValueError:
            print("Angka yang dimasukkan tidak valid!")

def addto_data():
    hasil = menghitung_gaji()
    if hasil is None:
        return
    
    nama, tambahan_panen = hasil

    for karyawan in data_panen:
        if karyawan["nama"] == nama:
            karyawan["total setoran"] += tambahan_panen
            break
    else:
        data_panen.append({"nama":nama,"total setoran":tambahan_panen})

def show_leaderboard():
    for i, selected_karyawan in enumerate(data_panen, start=1):
        print(f"\nPilih metode urut atau ketik 'cancel'")
        print("1. Waktu setoran pertama")
        print("2. Nama")
        print("3. Jumlah setoran tertinggi")
        metode_urut = input(": ").strip().lower()

        if metode_urut == "1":
            ranking = data_panen
        if metode_urut == "2":
            ranking = sorted(data_panen, key=lambda k: k["nama"])
        elif metode_urut == "3":
            ranking = sorted(data_panen, key=lambda k: k["total setoran"], reverse=True)
        elif metode_urut == "cancel":
            return
        else:
            print("Metode urut tidak ditemukan.")
            continue

        print("\n===LEADERBOARD===")
        for i, k in enumerate(ranking, start=1):
            print(f"{i}. {k['nama']} | {k['total setoran']} kg")
            continue
            
while True:
    print("\nMau ngapain hari ini, Peternak Lele?")
    print("1. Menghitung gaji")
    print("2. Lihat leaderboard")
    print("3. COMING SOON (jangan coba-coba)")
    print("4. Tutup program")

    pilihan = input(": ")
    if pilihan == "1":
        addto_data()
    elif pilihan == "2":
        show_leaderboard()
    elif pilihan == "3":
        print("Sudah dibilang COMING SOON itu kocak.")
    elif pilihan == "4":
        print("Dadah!")
        break
    else:
        print("Angka yang dimasukkan tidak valid!")