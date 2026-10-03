username_benar = "agamemnon67"
password_benar = "071"
saldo = 1000000

kesempatan = 3
while 0 < kesempatan <= 3:
    username = input("\nMasukkan username anda: ")
    password = input("Masukkan password anda: ")
    if username == username_benar and password == password_benar:
        print("\nLogin Berhasil!")
        break
    else: 
        kesempatan -= 1
        print(f"\nLogin Gagal! Sisa percobaan {kesempatan}")
        if kesempatan == 0:
            print("Akun Anda Terblokir!")
            exit()
        continue

while True:
    valid = False
    print("\n===MENU ATM===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")

    opsi = input(": ")

    if opsi == "1":
        print(f"Saldo anda: Rp. {saldo}")

    elif opsi == "2":
        tarik = input("\nMasukkan nominal tarik (kelipatan Rp.50000): Rp.")
        for char in tarik:
            if "0" <= char <= "9":
                valid = True
                continue
            else:
                valid = False
                print("Angka tidak valid!")
                break
        if valid == True:
            tarik = int(tarik)
            if tarik % 50000 == 0:
                if tarik > saldo and 0 <= tarik:
                    print("Saldo anda tidak mecukupi!")
                    print(f"Sisa saldo: Rp. {saldo}")
                else:
                    saldo -= tarik
                    print("Transaksi Berhasil!")
                    print(f"Sisa saldo anda: Rp. {saldo}")
            else:
                print("Nominal harus kelipatan Rp 50.000")
                continue

    elif opsi == "3":
        setor = input("Masukkan nominal setor (kelipatan Rp.50000): Rp.")
        for char in setor:
            if "0" <= char <= "9":
                valid = True
                continue
            else:
                print("Angka tidak valid!")
                valid = False
                continue
        setor = int(setor)
        if setor > 0:
            if setor % 50000 == 0:
                saldo += setor
                print(f"Berhasil menyetor Rp.{setor}")
                print(f"Total saldo anda Rp.{saldo}")
            else:
                print("Nominal harus kelipatan Rp 50.000")
        else:
            print("Nonimal setor tidak boleh kurang dari 0!")

    elif opsi == "4":
        print("Terima kasih!")
        exit()

    else:
        print("Opsi tidak ditemukan!")
        continue