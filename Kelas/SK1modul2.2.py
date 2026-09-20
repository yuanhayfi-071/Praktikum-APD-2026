# Seorang karyawan akan menerima gaji dari perusahaan ternak lele tempat ia
# bekerja dengan ketentuan sebagai berikut:
# ● Gaji pokok = 2.000.000
# ● Bonus total panen = Rp. 5.000/Kilogram
# ● Pph (Pajak Penghasilan) = 10% dari gaji pokok + bonus
# ● Total Gaji = (Gaji pokok + bonus) - Pph
# Buatkan program yang dapat menghitung total gaji karyawan tersebut dan
# tampilkan hasilnya!

gaji_pokok = 2000000

while True:
    print("\nMau ngapain hari ini, Peternak Lele?")
    print("1. Menghitung gaji")
    print("2. COMING SOON (jangan coba-coba)")
    print("3. COMING SOON (jangan coba-coba)")
    print("4. Tutup program")

    def menghitung_gaji():
        nama_karyawan = input("Masukkan nama anda: ").upper()    
        while True:
            panen_mentah = (input("Masukkan total panen anda (kg) atau ketik 'keluar': ")).lower().strip()
            if panen_mentah == "keluar":
                return
            try: 
                panen_int = int(panen_mentah)
                bonus = 5000 * panen_int
                pph = (gaji_pokok + bonus) * 0.1
                gaji_total = (gaji_pokok + bonus) - pph

                print("Nama: " + nama_karyawan)
                print(f"Jumlah panen: {panen_int} kg")
                print(f"Gaji anda (dipotong pajak: Rp. {gaji_total}")
                return
            except ValueError:
                print("Angka yang dimasukkan tidak valid!")
                


    pilihan = input(": ")
    if pilihan == "1":
        menghitung_gaji()
    elif pilihan in ["2","3"]:
        print("Sudah dibilang COMING SOON itu kocak.")
    elif pilihan == "4":
        break
    else:
        print("Angka yang dimasukkan tidak valid!")