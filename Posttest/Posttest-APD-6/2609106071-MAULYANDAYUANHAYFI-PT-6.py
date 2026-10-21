import os
import time

#Settingan login
data_login = {
    "admin":{"pw":"admin123", "akses":"admin"}
}

#Settingan game
RESTVAL = [20, 40]
TIMESTRESSVAL = [10, 15]
DEADLSTRESS = 50

pengaturan = {"bhari": 8, "bstress": 100, "utang": 1000, "bporto": 3}

#Setting kerjaan
all_job = [
    {"nproyek":"Desain Rumah Nyaman","stresscost":5,"bayaran":50,"tenggat":2},
    {"nproyek":"Desain Rumah Mewah","stresscost":15,"bayaran":125,"tenggat":3}, 
    {"nproyek":"Desain Toko Mewah","stresscost":10,"bayaran":115,"tenggat":3}
]

while True: #Main loop
    logged_in = False
    admin = False
    game_selesai = False
    intro = True

    while not logged_in:
        os.system('cls')
        print("\n","="*5,"SIMULASI HIDUP KAVEH", "="*5)
        print("Silahkan masuk ke akun anda.")
        print("1. Sudah punya akun -> Log in")
        print("2. Belum punya akun -> Sign in")
        opsi = input(": ")
        if opsi == "1":
            while True:
                input_usn = input("\nMasukkan nama pengguna atau '/kembali'.\n> ").strip().lower()
                usn_exist = data_login.get(input_usn)
                if input_usn == '/kembali':
                    print("Membersihkan terminal...")
                    time.sleep(1.5)
                    break
                elif usn_exist is None:
                    print(f"Nama pengguna {input_usn} tidak ditemukan.")
                    continue
                input_pw = input("Masukkan password.\n> ")
                if input_pw == data_login[input_usn]["pw"]:
                    logged_in = True
                    if usn_exist["akses"] == "admin":
                        admin = True
                    print(f"Login berhasil. Selamat datang, {input_usn}!")
                    break
                else:
                    print("Password salah!")
            
        elif opsi == "2":
            while True:
                input_usn = input("\nMasukkan nama pengguna baru atau '/kembali'.\n> ").strip().lower()
                usn_exist = data_login.get(input_usn)
                if input_usn == "/kembali":
                    print("Membersihkan terminal...")
                    break
                elif len(input_usn.strip()) == 0:
                    print("Nama pengguna tidak boleh kosong.")
                elif usn_exist:
                    print(f"Nama pengguna {input_usn} sudah ada.")
                else:
                    input_pw = input("Masukkan password baru.\n> ")
                    data_login.update({input_usn: {"pw":input_pw, "akses":"member"}})
                    print(f"\nAkun {input_usn} berhasil dibuat!")
                    print("Membersihkan terminal...")
                    break
        else:
            print("Opsi tidak ditemukan.")
        time.sleep(2)

    # Inisialisasi progress pemain
    hari = 1
    stress = 25 
    mora = 100
    waktu = ["Siang","Malam"]
    indekswaktu = 0
    proyek = []
    portofolio = []
    waitlist = []
    pos_job = [all_job[0]]

    while logged_in:
        if game_selesai == True:
            print("\n","="*5,f"HASIL SIMULASI {input_usn}","="*5)
            print(f"Hari    : {hari}/{pengaturan['bhari']}"\
                f"\nMora    : {mora}/{pengaturan['utang']}"\
                f"\nStress  : {stress}/{pengaturan['bstress']}")
            while True:
                kembali = input("\nKetik 'kembali' untuk ke halaman login.\n> ").strip().lower()
                if kembali == "kembali":
                    break
            print("Mengembalikan ke halaman login...")
            break

        if intro == True: #Intro day 1
            time.sleep(1.5)
            os.system('cls')
            if admin == True:
                print("\n","="*5,"BERMAIN DALAM MODE ADMIN","="*5)
            print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
            print(f"Ia punya utang {pengaturan['utang']} Mora yang harus dibayar {pengaturan['bhari']-1} hari lagi!")
            print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
            print(f"\nHINT: Bekerja menambah stress ({TIMESTRESSVAL[0]}/{TIMESTRESSVAL[1]}) di (siang/malam), "
            f"sedangkan Beristirahat mengurangi ({RESTVAL[0]}/{RESTVAL[1]}) di (siang/malam).")
            intro = False
 
        if len(portofolio) >= pengaturan['bporto']: #Kontrol porto
            pos_job = all_job
        else:
            pos_job = all_job[:1]
            
        if hari < pengaturan['bhari'] and stress < pengaturan['bstress']: #Siklus menu game
            print(f"\nKetik 'lh' untuk melihat perintah atau 'kembali' ke halaman login.")
            print(f"[Hari ke-{hari}/{pengaturan['bhari']}: {waktu[indekswaktu]}] [{mora}/{pengaturan['utang']} Mora]")
            perintah = input("> ")

            if perintah.strip().lower() == "kembali":
                print("\nMengembalikan ke halaman login...")
                time.sleep(1.5)
                break

            elif perintah.strip().lower() == "lh":
                os.system('cls')
                print("\n+ \nPERINTAH")
                print("ld   -> Detail status" \
                    "\nljs  -> Cari kerja" \
                    "\nlp   -> Kerja"
                    "\nlr   -> Istirahat")
                if admin == True:
                    print("led    -> Edit Sistem/Atribut" \
                    "\nlusd   -> Edit Data User")
                print("+")

            elif perintah.strip().lower() == "ld":
                os.system('cls')
                print("\n+ \nDETAIL STATUS")
                print(f"Mora: {mora}")
                print(f"Stress: {stress}")
                if not proyek:
                    print(f"\nProyek kosong, masih nganggur!")
                else:
                    print(f"\nproyek:")
                    for i, item in enumerate(proyek, start=1):
                        print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                if not portofolio:
                    print(f"\nPortofolio kosong, ayo kerja!")
                else:
                    print(f"\nPortofolio:")
                    for i, item in enumerate(portofolio, start=1):
                        print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora")
                print("+")

            elif perintah.strip().lower() == "ljs":
                print("\nMengecek papan informasi...")
                time.sleep(1.5)
                while True:
                    os.system('cls')
                    print("\n+ \nTAWARAN PROYEK")
                    for i, item in enumerate(pos_job, start=1):
                        print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                    print("+")
                    opsi = input("\nKetik 'ladd' satu atau beberapa '[INDEX]' untuk mengambil kerjaan atau 'kembali'.\n> ").lower()
                    bagian = opsi.split()
                    if not bagian:
                        continue
                    elif bagian[0] == "kembali":
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
                            time.sleep(1.5)
                            continue
                        else:
                            os.system('cls')
                            print("\nMemilih proyek:")
                            waitlist.sort(key=lambda k:k['nproyek'])
                            for i, item in enumerate(waitlist, start=1):
                                print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                            while True:    
                                confirm = input("\nKetik 'confirm' untuk konfirmasi atau 'kembali'.\n> ")
                                if confirm.strip().lower() == 'confirm':
                                    print("\nDikonfirmasi!")
                                    proyek.extend(waitlist)
                                    break
                                elif confirm.strip().lower() == 'kembali':
                                    print("\nDibatalkan!")
                                    break
                    else:
                        print("Perintah tidak dikenali.")
                    time.sleep(1.5)

            elif perintah.strip().lower() == "lp":
                while True:
                    os.system('cls')
                    if not proyek:
                        print("\nProyek kosong, masih nganggur!")
                        break
                    else:
                        print(f"\nProyek:")
                        for i, item in enumerate(proyek, start=1):
                            print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora | Stress: {item['stresscost']} | Tenggat: {item['tenggat']}")
                                        
                        opsi = input("\nKetik satu '[INDEX]' untuk dituntaskan atau 'kembali'.\n> ")
                        if opsi.strip().lower() == "kembali":
                            print("Batal bekerja...")
                            break
                        elif opsi.isdigit() and 1 <= int(opsi) <= len(proyek):
                            opsi = int(opsi)
                            print("Kaveh bekerja dengan rajin...")
                            time.sleep(2)
                            os.system('cls')
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
                            if stress >= pengaturan['bstress'] or hari >= pengaturan['bhari']:
                                break
                        else:
                            print("Indeks tidak ditemukan!")
                        time.sleep(2)
                        os.system('cls')

            elif perintah.strip().lower() == "lr":
                os.system('cls')
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

            elif perintah.strip().lower() == "led" and admin == True:
                while True:
                    os.system('cls')
                    print("\nSISTEM")
                    print(f"1. Batas hari   : {pengaturan['bhari']}"\
                        f"\n2. Batas stress : {pengaturan['bstress']}"\
                        f"\n3. Utang        : {pengaturan['utang']}"\
                        f"\n4. Semua proyek : ")
                    for item in all_job:
                        print(f"- {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                    
                    print("\nATRIBUT")
                    print(f"5. Hari ke- :{hari}"\
                        f"\n6. Mora     : {mora}"\
                        f"\n7. Stress   : {stress}")
                
                    pilih_edit = input("\nKetik [INDEKS] pengaturan untuk diedit atau 'kembali'.\n> ").strip().lower()
                    if pilih_edit == "kembali":
                        os.system('cls')
                        break

                    elif pilih_edit in ["1", "2", "3"]:
                        indeks = list(pengaturan)[int(pilih_edit) - 1]
                        while True:
                            baru = input(f"\nMasukkan nilai baru untuk pengaturan {pilih_edit} atau 'kembali': ")
                            if baru == "kembali":
                                break
                            elif baru.isdigit() and int(baru) > 0:
                                pengaturan[indeks] = int(baru)
                                print(f"Pengaturan {pilih_edit} diubah menjadi {pengaturan[indeks]}.")
                                break
                            else:
                                print("Nilai harus berupa angka dan lebih dari 0.")
                    
                    elif pilih_edit == "4":
                        while True:
                            pilihan = input("\nKetik 'lnew' untuk membuat proyek baru, 'ledj' untuk mengedit,\natau 'kembali': ")
                            if pilihan == "kembali":
                                break

                            elif pilihan == "lnew":
                                npname = input("\nMasukkan nama proyek baru: ")
                                while True:
                                    npstress = input("Masukkan angka stress: ")
                                    if npstress.isdigit() and int(npstress) > 0:
                                        break
                                    else:
                                        print("\nStress harus berupa angka dan lebih dari 0.")
                                        continue
                                while True:
                                    npmora = input("Masukkan bayaran: ")
                                    if npmora.isdigit() and int(npmora) > 0:
                                        break
                                    else:
                                        print("\nMora harus berupa angka dan lebih dari 0.")
                                        continue
                                while True:
                                    nptenggat = input("Masukkan tenggat: ")
                                    if nptenggat.isdigit() and int(nptenggat) > 0:
                                        break
                                    else:
                                        print("\nTenggat harus berupa angka dan lebih dari 0.")
                                        continue
                                proyekbaru = {"nproyek":npname,"stresscost":int(npstress),"bayaran":int(npmora),"tenggat":int(nptenggat)}
                                all_job.append(proyekbaru)
                                print(f"\nProyek {proyekbaru['nproyek']} | Stress: {proyekbaru['stresscost']} | {proyekbaru['bayaran']} Mora | Tenggat: {proyekbaru['tenggat']} berhasil ditambahkan!")

                            elif pilihan == "ledj":
                                print("")
                                for i, item in enumerate(all_job,start=1):
                                    print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                                while True:
                                    pindex = input("\nMasukkan [INDEKS] untuk diedit atau 'kembali'.\n> ")
                                    if pindex == "kembali":
                                        break
                                    
                                    elif pindex.isdigit() and 0 <= int(pindex) -1 < len(all_job):
                                        selected_job = all_job[int(pindex)-1]
                                        print("\nAtribut yang bisa diedit:"\
                                            f"\n1. Nama Proyek  -> 'nproyek'"\
                                            f"\n2. Stress       -> 'stresscost'"\
                                            f"\n3. Bayaran      -> 'bayaran'"\
                                            f"\n4. Tenggat      -> 'tenggat'")
                                        atribut = input("\nKetik nama atribut untuk diedit.\n> ")
                                        if atribut in selected_job:
                                            patribut = selected_job[atribut]
                                            natribut = input(f"\nMasukkan nilai {atribut} baru: ")
                                            if atribut != 'nproyek' and natribut.isdigit() and int(natribut) > 0:
                                                selected_job[atribut] = int(natribut)
                                                print(f"\nMengedit {selected_job['nproyek']} | Nilai awal: {patribut}, Nilai akhir: {natribut}!")
                                                break
                                            elif atribut == 'nproyek':
                                                selected_job[atribut] = natribut
                                                break
                                            else:
                                                print("Nilai harus berupa angka dan lebih dari 0.")
                                        else:
                                            print(f"Atribut {atribut} tidak ditemukan.")
                                    else:
                                        print("Indeks harus berupa angka dan terdapat di list.")
                    
                    elif pilih_edit == "5":
                        while True:
                            nhari = input("\nMasukkan hari baru atau 'kembali': ")
                            if nhari == "kembali":
                                break
                            elif nhari.isdigit() and int(nhari) > 0:
                                hari = int(nhari)
                                print(f"Hari diubah menjadi {hari}.")
                                break
                            else:
                                print("Hari harus berupa angka dan lebih dari 0.")
                    
                    elif pilih_edit == "6":
                        while True:
                            nmora = input("\nMasukkan mora baru atau 'kembali': ")
                            if nmora == "kembali":
                                break
                            elif nmora.isdigit() and int(nmora) >= 0:
                                mora = int(nmora)
                                print(f"Mora diubah menjadi {mora}.")
                                break
                            else:
                                print("Mora harus berupa angka.")
                    
                    elif pilih_edit == "7":
                        while True:
                            nstress = input("\nMasukkan stress baru atau 'kembali': ")
                            if nstress == "kembali":
                                break
                            elif nstress.isdigit() and int(nstress) >= 0:
                                stress = int(nstress)
                                print(f"Stress diubah menjadi {stress}.")
                                break
                            else:
                                print("Stress harus berupa angka dan bernilai 0 atau lebih.")
                    
                    else:
                        print("Indeks tidak ditemukan.")
                    time.sleep(2)

            elif perintah.strip().lower() == "lusd" and admin == True:
                while True:    
                    os.system('cls')
                    print("\nDAFTAR PENGGUNA")
                    for i, user in enumerate(data_login,start=1):
                        print(f"{i}. {user} | Akses: {data_login[user]['akses']}")
                    pilihan = input("\nKetik 'lacs' untuk mengubah akses, 'lrem' untuk menghapus akun, atau 'kembali'.\n> ").strip().lower()
                    
                    if pilihan == "kembali":
                        os.system('cls')
                        break
    
                    elif pilihan == "lacs":
                        nama = input("\nKetik nama akun untuk diubah aksesnya.\n> ").strip().lower()
                        if nama in data_login:
                            if nama == input_usn:
                                print("Tidak bisa mengedit akun yang sedang digunakan.")
                            else:
                                akses_ubahke = input("\nKetik untuk mengubah akses ke 'admin' atau 'member'.\n> ").strip().lower()
                                if akses_ubahke == "admin" or akses_ubahke == "member":
                                    if data_login[nama]["akses"] != akses_ubahke:
                                        print(f"Akses {nama} diubah menjadi {akses_ubahke}.")
                                        data_login[nama]["akses"] = akses_ubahke
                                    else:
                                        print(f"Akses {nama} sudah {akses_ubahke}.")
                                else:
                                    print(f"Akses {akses_ubahke} tidak ditemukan.")
                        else:
                            print("Akun tidak ditemukan.")
                    
                    elif pilihan == "lrem":
                        nama = input("\nKetik nama akun yang ingin dihapus.\n> ").strip().lower()
                        if nama in data_login:
                            if nama == input_usn:
                                print("Tidak bisa menghapus akun yang sedang digunakan.")
                            else:
                                while True:
                                    confirmhapus = input(f"\nKetik 'confirm' untuk menghapus {nama} atau 'kembali'.\n> ").strip().lower()
                                    if confirmhapus == "confirm":
                                        del data_login[nama]
                                        print(f"Pengguna {nama} dihapus!")
                                        break
                                    elif confirmhapus == "kembali":
                                        break
                        else:
                            print("Akun tidak ditemukan.")
                    else:
                        print("Perintah tidak ditemukan.")
                    time.sleep(2)

        elif stress >= pengaturan['bstress']: #Death flag
            print(f"Tingkat stress: {stress}")
            print("\nKaveh jatuh dalam keterpurukan.")
            print("GAME OVER!")
            game_selesai = True
        
        elif hari >= pengaturan['bhari']: #Ending
            time.sleep(2)
            os.system('cls')
            print(f"\nHari ke-{pengaturan['bhari']-1} telah berlalu. Saatnya bayar utang.")
            if mora < pengaturan['utang']:
                print(f"Bad ending! Mora {mora} kurang dari {pengaturan['utang']}.") 
                print(f"Kaveh harus berlutut pada Alhaitham!")
            else:
                print(f"Good ending! Mora {mora}. Kaveh membayar utangnya pada Alhaitham.")
            game_selesai = True