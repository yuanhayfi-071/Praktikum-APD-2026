#Settingan login
data_login = {
    "admin":{"pw":"admin123", "akses":"admin"}
}

#Settingan game
batas_hari = 8
batas_stress = 100
utang = 1000
RESTVAL = [20, 40]
TIMESTRESSVAL = [10, 15]
DEADLSTRESS = 50

while True: #Main loop
    logged_in = False
    admin = False
    game_selesai = False
    intro = True

    while not logged_in:
        print("\nSilahkan masuk ke akun anda.")
        print("1. Sudah punya akun -> Log in")
        print("2. Belum punya akun -> Sign in")
        opsi = input(": ")
        if opsi == "1":
            input_usn = input("Username: ")
            input_pw = input("Password: ")
            usn_exist = data_login.get(input_usn)
            if usn_exist == None:
                print(f"Nama pengguna {input_usn} tidak ditemukan.")
                continue
            elif input_pw == data_login[input_usn]["pw"]:
                logged_in = True
                if usn_exist["akses"] == "admin":
                    admin = True
                print(f"Login berhasil. Selamat datang, {input_usn}!")
            else:
                print("Password salah.")
            
        elif opsi == "2":
            input_usn = input("Masukkan nama pengguna baru: ")
            usn_exist = data_login.get(input_usn)
            if usn_exist == None:
                input_pw = input("Masukkan password baru: ")
                data_login.update({input_usn: {"pw":input_pw, "akses":"member"}})
                print(f"Akun {input_usn} berhasil dibuat!")
            else:
                print(f"Nama pengguna {input_usn} sudah ada.")
        else:
            print("Opsi tidak ditemukan.")

    while logged_in:
        # Inisialisasi progress pemain
        hari = 1
        stress = 25 #Death flag: stress >= 100
        mora = 100 #Objektif: bayar utang 1k Mora di hari ke-8
        waktu = ["Siang","Malam"]
        indekswaktu = 0
        proyek = []
        portofolio = []
        waitlist = []
        pos_job = [{"nproyek":"Desain Rumah Nyaman","stresscost":5,"bayaran":50,"tenggat":2}]

        if game_selesai == True:
            print(f"\nHASIL SIMULASI {input_usn}")
            print(f"Hari    : {hari}/{batas_hari}"\
                  f"\nMora    : {mora}/{utang}")
            while True:
                kembali = input("\nKetik 'kembali' untuk ke halaman login.").strip().lower()
                if kembali == "kembali":
                    break
            print("Mengembalikan ke halaman login...")
            break

        if intro == True: #Intro day 1
            if admin == True:
                print("\nBERMAIN DALAM MODE ADMIN")
            print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
            print("Ia punya utang 1k Mora yang harus dibayar 7 hari lagi!")
            print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
            print(f"\nHINT: Bekerja menambah stress ({TIMESTRESSVAL[0]}/{TIMESTRESSVAL[1]}) di (siang/malam),"
            f"sedangkan Beristirahat mengurangi ({RESTVAL[0]}/{RESTVAL[1]}) di (siang/malam).")
            print(f"Ketik 'lh' untuk melihat perintah atau 'kembali' ke halaman login.")
            intro = False
 
        if len(pos_job) == 1 and len(portofolio) >= 3: #Kontrol porto
            pos_job.extend([
                {"nproyek":"Desain Rumah Mewah","stresscost":15,"bayaran":125,"tenggat":3}, 
                {"nproyek":"Desain Toko Mewah","stresscost":10,"bayaran":115,"tenggat":3}
                ])
            
        if hari < batas_hari and stress < batas_stress: #Siklus utama game
            print(f"\n[Hari ke-{hari}/{batas_hari}: {waktu[indekswaktu]}] [{mora}/{utang} Mora]")
            perintah = input("\n> ")

            if perintah.strip().lower() == "kembali":
                print("\nMengembalikan ke halaman login...")
                break

            elif perintah.strip().lower() == "lh":
                print("\n+ \nPERINTAH")
                print("ld   -> Detail status" \
                    "\nljs  -> Cari kerja" \
                    "\nlp   -> Kerja"
                    "\nlr   -> Istirahat")
                if admin == True:
                    print("led    -> Edit")
                print("+")

            elif perintah.strip().lower() == "ld":
                print("\n+ \nDETAIL STATUS")
                print(f"Mora: {mora}")
                print(f"Stress: {stress}")
                if not proyek:
                    print(f"\nProyek kosong, masih nganggur!")
                else:
                    print(f"\nProyek:")
                    for i, item in enumerate(proyek, start=1):
                        print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                if not portofolio:
                    print(f"\nPortofolio kosong, ayo kerja!")
                else:
                    print(f"\nPortofolio:")
                    for i, item in enumerate(portofolio, start=1):
                        print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora")
                print("+")

            elif perintah.strip().lower() == "ljs":
                print("\nMengecek papan informasi...")
                print("\n+ \nTAWARAN PROYEK")
                for i, item in enumerate(pos_job, start=1):
                    print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                print("+")

                while True: #Mengambil kerja
                    opsi = input("\nKetik 'ladd' satu atau beberapa '[INDEX]' untuk mengambil kerjaan atau 'cancel'.\n> ").lower()
                    bagian = opsi.split()
                    if not bagian:
                        continue
                    elif bagian[0] == "cancel":
                        print("\nPergi dari papan informasi...")
                        break
                    elif bagian[0] == "ladd" and all(x.isdigit() for x in bagian[1:len(bagian)]):
                        waitlist.clear()
                        for x in bagian[1:len(bagian)]:
                            i = int(x)
                            if 1 <= i <= len(pos_job):
                                waitlist.append(pos_job[i-1].copy())
                        if not waitlist:
                            print("Indeks tidak ditemukan!")
                            continue
                        else:
                            print("\nMemilih proyek:")
                            waitlist.sort(key=lambda k:k['nproyek'])
                            for i, item in enumerate(waitlist, start=1):
                                print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                            while True:    
                                confirm = input("\nKetik 'confirm' untuk konfirmasi atau 'cancel'.\n> ")
                                if confirm.strip().lower() == 'confirm':
                                    print("\nDikonfirmasi!")
                                    proyek.extend(waitlist)
                                    break
                                elif confirm.strip().lower() == 'cancel':
                                    print("\nDibatalkan!")
                                    break

            elif perintah.strip().lower() == "lp":
                    while True:
                        if not proyek:
                            print("\nProyek kosong, masih nganggur!")
                            break
                        else:
                            print(f"\nProyek:")
                            for i, item in enumerate(proyek, start=1):
                                print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora | Stress: {item['stresscost']} | Tenggat: {item['tenggat']}")
                                            
                            opsi = input("\nKetik satu '[INDEX]' untuk dituntaskan atau 'cancel'.\n> ")
                            if opsi == "cancel":
                                print("\nBatal bekerja...")
                                break
                            elif opsi.isdigit():
                                opsi = int(opsi)
                                if 1 <= opsi <= len(proyek):
                                    print("\nKaveh bekerja dengan rajin...")
                                    terselesaikan = proyek.pop(opsi-1)
                                    portofolio.append(terselesaikan)
                                    print(f"{terselesaikan['nproyek']} terselesaikan!")
                                    mora += terselesaikan['bayaran']
                                    print(f"Mora +{terselesaikan['bayaran']}")
                                    stress += TIMESTRESSVAL[indekswaktu] + terselesaikan['stresscost']
                                    print(f"Stress +{(TIMESTRESSVAL[indekswaktu]) + terselesaikan['stresscost']}")

                                    indekswaktu = (indekswaktu + 1) % len(waktu)
                                    print(f"\nWaktu berlalu... Sekarang {waktu[indekswaktu]}.")
                                    if indekswaktu == 0:
                                        print("Sehari terlewati...")
                                        hari += 1
                                        sisa = [] #Menampung proyek2 yg tenggatnya blm habis saat disaring
                                        for i, item in enumerate(proyek):
                                            item['tenggat'] -= 1
                                            if item['tenggat'] <= 0:
                                                stress += DEADLSTRESS
                                                print(f"Tenggat {item['nproyek']} terlewat! Stress +{DEADLSTRESS}")
                                            else:
                                                sisa.append(item)
                                        proyek[:] = sisa
                                    if stress >= 100 or hari >= 8:
                                        break
                                        
                                else:
                                    print("Indeks tidak ditemukan!")
                            else:
                                print("Indeks harus berupa satu angka!")

            elif perintah.strip().lower() == "lr":
                print("Kaveh memilih tidur di rumah...")

                stress -= RESTVAL[indekswaktu]
                if stress < 0:
                    stress = 0
                print(f"Stress -{RESTVAL[indekswaktu]}")
                print("Kaveh merasa segar kembali!")
                print(f"Tingkat stress: {stress}")

                indekswaktu = (indekswaktu + 1) % len(waktu)
                print(f"\nWaktu berlalu... Sekarang {waktu[indekswaktu]}.")
                if indekswaktu == 0:
                    print("Sehari terlewati...")
                    hari += 1
                    sisa = []
                    for i, item in enumerate(proyek):
                        item['tenggat'] -= 1
                        if item['tenggat'] <= 0:
                            stress += DEADLSTRESS
                            print(f"Tenggat {item['nproyek']} terlewat! Stress +{DEADLSTRESS}")
                        else:
                            sisa.append(item)
                    proyek[:] = sisa
                if stress >= 100 or hari >= 8:
                    continue

            elif perintah.strip().lower() == "led" and admin == True:
                print("\nSISTEM")
                print(f"1. Batas hari   : {batas_hari}"\
                      f"\n2. Batas stress : {batas_stress}"\
                      f"\n3. Utang        : {utang}"\
                      f"\n4. Papan kerja  : ")
                for item in pos_job:
                    print(f"- {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                
                print("\nATRIBUT")
                print(f"1. Hari ke-{hari}"\
                      f"\n2. Mora     : {mora}"\
                      f"\n3. Stress   : {stress}")
                
                while True:
                    pilih_edit = input("\nKetik [INDEKS] pengaturan untuk diedit atau 'kembali'.\n> ")
                    if pilih_edit == "1":
                        nbatas_hari = input("\nBatas hari baru: ")
                        if nbatas_hari.isdigit() and int(nbatas_hari) > 0:
                            batas_hari = int(nbatas_hari)
                            print(f"Batas hari diubah menjadi {batas_hari}.")
                        else:
                            print("Batas hari harus berupa angka dan lebih dari 0.")
                    elif pilih_edit == "kembali":
                        break
                    else:
                        print("Indeks tidak ditemukan.")

        elif stress >= batas_stress: #Death flag
            print(f"Tingkat stress: {stress}")
            print("\nKaveh jatuh dalam keterpurukan.")
            print("GAME OVER!")
            game_selesai = True
        
        elif hari == batas_hari: #Ending
            print("\nHari ke-7 telah berlalu. Saatnya bayar utang.")
            if mora < utang:
                print(f"Bad ending! Mora {mora} kurang dari {utang}.") 
                print(f"Kaveh harus berlutut pada Alhaitham!")
            else:
                print(f"Good ending! Mora {mora}. Kaveh membayar utangnya pada Alhaitham.")
            break