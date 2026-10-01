#tata_fitur:
# 1. menu top up
# 2. kategori top up
# 3. metode pembayaran
# 4. biaya admin
# 5. hitung total bayar
# 6. minta input bayar
# 7. tampilkan struk pembelian

akun = [{"nama_akun":"Maul", "password":"71"}]
logged_in = False
daftar_game = ["Genshin Impact", "Minecraft", "Mobile Legends: Bang Bang"]

def login_menu():
    print("\nSilahkan masuk ke akun anda.")
    print("1. Sudah punya akun -> Log in")
    print("2. Belum punya akun -> Sign in")
    opsi = input(": ")
    if opsi == "1":
        login()
    elif opsi == "2":
        sign_in()
    else:
        print("Opsi tidak ditemukan.")

def login():
    global logged_in
    input_nama = input("\nMasukkan nama akun: ")
    akun_ditemukan = False
    for i in akun:
        if i["nama_akun"] == input_nama:
            password = input("Masukkan password: ")
            akun_ditemukan = True
            if password == i["password"]:
                print("Login berhasil.")
                print(f"\nSelamat datang, {input_nama}!")
                logged_in = True
            else:
                print("Login gagal.")
                print("Password yang dimasukkan salah!") 
            break
    if not akun_ditemukan:
        print("Akun tidak ditemukan.")

def sign_in():
    akun_baru = input("\nMasukkan nama akun baru: ")
    while any(n["nama_akun"] == akun_baru for n in akun):
        print("Nama akun telah dipakai.")
        akun_baru = input("Masukkan nama akun baru: ")
    else:
        password = input("Masukkan password baru: ")
        akun.append({"nama_akun": akun_baru, "password": password})
        print(f"\nAkun {akun_baru} selesai dibuat!")
        print(f"Anda akan kembali ke halaman login.")

def katalog():
    while True:
        global logged_in
        global game
        print("\n===KEQINGTOPUP.COM===")
        print("Silhkan pilih game atau ketik 'exit'.")
        print("1. Genshin Impact")
        print("2. Minecraft")
        print("3. Mobile Legends: Bang Bang")

        opsi = input(": ").strip()
        if opsi.lower() == "exit":
            return #return biar kembali ke login
        try:
            opsi = int(opsi)
        except ValueError:
            print("Opsi harus berupa angka.")
            continue #continue biar kembali ke while opsi: milih game
        if 0 < opsi <= len(daftar_game):
            game = daftar_game[opsi -1]
        else:
            print("Opsi tidak ditemukan.")
            continue
        while True:
            print("\nMasukkan player ID, atau ketik 'cancel'.") #memasukkan player id + siapa tahu salah milih game
            player_id = input(": ").strip()
            if player_id.lower() == "cancel":
                break #break biar kembali ke while opsi: milih game
            if not player_id:
                print("Player ID tidak boleh kosong.")
                continue
            return game, player_id

def memilih_kategori_topup():
    while True:
        global kategori_topup
        global harga_dasar
        print("\nPilih kategori top up atau ketik 'cancel'.")
        print("1. Rp.15000 (Kecil)")
        print("2. Rp.50000 (Sedang)")
        print("3. Rp.150000 (Besar)")
        opsi = input(": ")
        if opsi == "1":
            kategori_topup = "Kecil"
            harga_dasar = 15000
            return kategori_topup, harga_dasar
        elif opsi == "2":
            kategori_topup = "Sedang"
            harga_dasar = 50000
            return kategori_topup, harga_dasar
        elif opsi == "3":
            kategori_topup = "Besar"
            harga_dasar = 150000
            return kategori_topup, harga_dasar
        elif opsi == "cancel":
            return
        else:
            print("Opsi tidak ditemukan.")
            continue

def admin():
    while True:
        print("\nPilih metode pembayaran")
        print("1. Pulsa")
        print("2. E-Wallet")
        opsi = input(": ")
        if opsi == "1" or opsi == "2":
            biaya_admin = 2500 if opsi == "1" else 500 
            metode_pembayaran = "Pulsa" if opsi == "1" else "E-Wallet"
            return biaya_admin, metode_pembayaran
        else:
            print("Opsi pembayaran tidak ditemukan.")
            continue

def pembayaran():
    while True:
        print(f"\nTotal Tagihan: Rp.{total_biaya}")
        setoran = input("Masukkan nominal pembayaran: Rp.")
        try:
            setoran = int(setoran)
        except ValueError:
            print("Nominal harus berupa angka.")
            continue
        if setoran < total_biaya:
            print("Transaksi gagal! Saldo tidak mencukupi.")
            continue
        elif setoran > total_biaya:
            kembalian = setoran - total_biaya
        else:
            kembalian = 0
        return kembalian, setoran

def print_struk():
    print("\n===KEQINGTOPUP.COM===")
    print(f"\nGame                : {game}")
    print(f"Player ID           : {player_id}")
    print(f"Kategori Topup      : {kategori_topup}")
    print(f"Metode Pembayaran   : {metode_pembayaran}")
    print(f"Biaya Admin         : Rp.{biaya_admin}")
    print(f"Total Tagihan       : Rp.{total_biaya}")
    print(f"Anda membayar       : Rp.{setoran}")
    if kembalian > 0:
        print(f"Kembalian           : Rp.{kembalian}")
    print("=======================")

print("\n===KEQINGTOPUP.COM===")
while True:
    while not logged_in:
        login_menu()

    while logged_in:
        hasil = katalog() #fungsi dijalankan sekaligus return value disimpan di hasil
        if hasil == None:
            logged_in = False
            continue
        else:
            game, player_id = hasil #mengekstrak return value yg ada lebih dari 1
            hasil = memilih_kategori_topup()
            if hasil == None:
                continue
            else:
                kategori_topup, harga_dasar = hasil
                biaya_admin, metode_pembayaran = admin()
                total_biaya = harga_dasar + biaya_admin
                kembalian, setoran = pembayaran()
                print_struk()