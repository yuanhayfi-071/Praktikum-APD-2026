#tata_fitur:
# 1. menu top up
# 2. kategori top up
# 3. metode pembayaran
# 4. biaya admin
# 5. hitung total bayar
# 6. minta input bayar
# 7. tampilkan struk pembelian

lanjut_topup = False
transaksi_berhasil = False
ada_kembalian = False
username_benar = "Maul"
password_benar = "71"
daftar_game = ["Genshin Impact","Minecraft","Mobile Legends"]
harga = [15000,50000,150000]

print("\n===KEQINGTOPUP.COM===")
print("Silahkan login terlebih dahulu.")
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == username_benar and password == password_benar: 
    print("\nLogin berhasil!")
    print(f"Selamat datang, {username}!")
    lanjut_topup = True
else:
    print("Login gagal!")

if lanjut_topup == True:
    print("\n===KEQINGTOPUP.COM===")
    player_id = input("Masukkan player ID: ")

    print("\nSilahkan pilih game.")
    print(f"1. {(daftar_game)[0]}")
    print(f"2. {(daftar_game)[1]}")
    print(f"3. {(daftar_game)[2]}")
    pilihan_game = int(input(": "))
    game = daftar_game[pilihan_game-1]
    print(f"\nAnda memilih {game}!")

    print("\nSilahkan pilih kategori top up:")
    print(f"1. Kecil Rp.{(harga)[0]}.")
    print(f"2. Sedang Rp.{(harga)[1]}.")
    print(f"3. Besar Rp.{(harga)[2]}.")
    pilihan_kategori = input(": ")
    if pilihan_kategori == "1":
        kategori_topup = "Kecil"
        harga_dasar = 15000
    elif pilihan_kategori == "2":
        kategori_topup = "Sedang"
        harga_dasar = 50000
    else:
        kategori_topup = "Besar"
        harga_dasar = 150000
    print(f"\nAnda memilih kategori {kategori_topup}!")

    print("\nPilih metode pembayaran:")
    print("1. Pulsa -> admin Rp.2500")
    print("2. E-Wallet -> admin Rp.500")
    pilihan_metode = input(": ")
    biaya_admin = 2500 if pilihan_metode == "1" else 500
    metode_pembayaran = "Pulsa" if pilihan_metode == "1" else "E-Wallet"
    print(f"\nAnda memilih metode pembayaran {metode_pembayaran}!")
    print(f"Pembelian dikenakan biaya admin Rp.{biaya_admin}.")

    total_bayar = harga_dasar + biaya_admin
    print(f"\nTotal tagihan anda Rp.{total_bayar}.")
    setoran = int(input("Masukkan nominal pembayaran: "))
    if setoran > total_bayar:
        kembalian = setoran - total_bayar
        ada_kembalian = True
        print("Transaksi berhasil!")
        transaksi_berhasil = True
    elif setoran == total_bayar:
        print("Transaksi berhasil!")
        transaksi_berhasil = True
    else:
        print("Transaksi gagal! Saldo tidak mencukupi.")

    if transaksi_berhasil == True:
        print("\n===KEQINGTOPUP.COM===")
        print(f"Player ID: {player_id}")
        print(f"Game: {game}")
        print(f"Kategori Top Up: {kategori_topup}")
        print(f"Metode Pembayaran: {metode_pembayaran}")
        print(f"Biaya Admin: Rp.{biaya_admin}")
        print(f"Total Tagihan: Rp.{total_bayar}")
        print(f"Nominal Pembayaran: Rp.{setoran}")
        if ada_kembalian == True:
            print(f"Kembalian: Rp.{kembalian}")
        print("\nTerima kasih telah Top Up di KEQINGTOPUP.COM!")


