    # 1. Diketahui Mas Elon Musk membeli 6 komponen roket rakitan yang dia beli di bengkel "Maju Mundur". Harga komponen yang dibeli adalah sebagai berikut: 
    # komponen_1 = 120000 
    # komponen_2 = 135000 
    # komponen_3 = 150000
    # komponen_4 = 175000
    # komponen_5 = 200000
    # komponen_6 = 220000
    # 2. Karena Mas Elon Musk meminta nota fisik dicetak premium, ia dikenakan biaya administrasi sebesar Rp15.000. Hitung total biaya yang harus dibayar! (Hitung manual ya, gak boleh pakai sum(  ), simpan di variabel total_biaya)

    # 3. Hitung rata-rata dengan membuat variabel bernama rata_rata (total_biaya dibagi banyak data, boleh pakai len(  ))
    # 4. Buat variabel bernama nim yang diisi dengan 2 digit nim terakhir.
    # 5. Buat variabel bernama bolean yang isinya nim != rata_rata
    # 6. Tampilkan semua variabel dengan menggunakan perintah print(  )

    # Poin Plus (+):
    # - Menggunakan list (masukkan isi komponen_1 dst ke dalam list yang bernama harga_komponen)
    # - Konversikan total_biaya ke mata uang Poundsterling (GBP) (bikin variabel sendiri)
    # - Tampilkan isi komponen_1 hingga komponen_4 dengan metode slice index negatif

biaya_komponen = 0

daftar_komponen = {
    1: {"nama":"komponen_1", "harga":120000}, 
    2: {"nama":"komponen_2", "harga":135000}, 
    3: {"nama":"komponen_3","harga":150000}, 
    4: {"nama":"komponen_4","harga":175000}, 
    5: {"nama":"komponen_5","harga":200000}, 
    6: {"nama":"komponen_6","harga":220000}
    }

print(f"\n{daftar_komponen}")
pesanan = input("\nMau beli apa, Bang? (contoh: 1, 2, 4): ")
pesanan_bersih = pesanan.split(",") #memisahkan perkoma

for str_pesanan in pesanan_bersih:
    str_pesanan = str_pesanan.strip() #ngilangin spasi
    if str_pesanan.isdigit(): #cek str_pesanan sudah berupa angka
        id_pesanan = int(str_pesanan) #menjadikan str_pesanan angka
        if id_pesanan in daftar_komponen: 
            harga_komponen = daftar_komponen[id_pesanan]["harga"]
            biaya_komponen += harga_komponen

premium = input("Cetak nota premium? (yes/no): ").lower().strip()
if premium == "yes":
    biaya_admin = 15000
else:
    biaya_admin = 0

biaya_total = biaya_komponen + biaya_admin
print(f"Total yang harus dibayar adalah: Rp.{biaya_total}")