#Settingan game
hari = 1
lokasi = "Rumah"
stress = 25
uang = 100

#Variabel
ADDSTRESS = [5,15,25] #minor (diganggu Hayi,etc.); kena sial; fucked up (miss tenggat, etc.)

#Settingan waktu
waktu = ["Pagi","Siang","Sore","Malam"]
indekswaktu = 0

#Kerjaan, maxout ending Light of Kshahrewar
proyek = []
portofolio = []
pos_job = [{"nproyek":"Desain Rumah Nyaman","progress":1,"stresscost":5,"bayaran":50,"tenggat":2},
        {"nproyek":"Desain Rumah Mewah","progress":3,"stresscost":15,"bayaran":145,"tenggat":3}, 
        {"nproyek":"Desain Toko Mewah","progress":2,"stresscost":10,"bayaran":115,"tenggat":2}]

#Detail status
mood = "Netral" #: sedih, ceroboh & tidak efisiesn; senang, kreatif & efisien
status = [] #: mabuk, rawan dijambret; dikutuk, ;diberkati
karma = 0 # <25, bepergian bisa dapat mora, nyari kerja lancar; >50, bepergian malam bisa dijambret

#Daftar fungsi
def time_pass():
    indekswaktu = (indekswaktu + 1) % len(waktu)
    if indekswaktu == 0:
        print("Sehari telah berlalu...")
        hari += 1

def show_perintah():
    print("\nDAFTAR PERINTAH")

def detail():
    print(f"\n=====DETAIL====="
            f"\nStatus = {status}"
            f"\nMood = {mood}"
            f"\nKarma = {karma}")
    if not proyek:
        print("proyek = Kosong, masih nganggur")
    else:
        for i, daftar in enumerate(proyek, start=1):
            print(f"{i}. proyek: {daftar['nproyek']} | Tenggat: {daftar['tenggat']}")

def job_search():
    print("\n=====MENCARI KERJA=====")
    print("1. Pasang brosur")
    print("2. Datangi Dori si pengusaha (agak kikir)")
    print("3. Datangi Nahida sang dewi")
    metode = input("\n> ")

    if metode == "1":
        if len(portofolio) <= 3:
            tambahkan = pos_job([1]).copy()
            proyek.append(tambahkan)
            print(f"\nProyek '{tambahkan['nproyek']}' didapat!")
        else:
            proyek.append({"nproyek":"Desain Interior Mahal","tenggat":5,"progress":0})

def show_map():
    print("\n===LOKASI===")
    print("1. Rumah" \
    "\n2. Tavern" \
    "\n3. Akademiya" \
    "\n4. Grand Bazaar" \
    "\n5. Gandhara Vile" \
    "\n6. Aaru Village" \
    "\n7. Port Ormos")
    tujuan = input("\nPilih indeks lokasi.\n> ")
    return tujuan

def walk_home():
    if lokasi != "Rumah":
        lokasi = "Rumah"
        print("Mau ngapain di rumah?")
        print("1. Menyibukkan diri"
        "\n2. Tidur")
        if indekswaktu == "Sore":
            print("\n3. Ganggu Alhaitham")
        kegiatan = input("\n> ")

        if kegiatan == "1":
            if not proyek:
                if indekswaktu == 0:
                    print("\nAlhaitham: 'Nganggur, ya?'")
                    print("Stress +5")
                    stress += 5
                elif indekswaktu == 1:
                    print("\nAlhaitham yang baru pulang kerja mendapati kamu sedang lap lemari.")
                    print("Alhaitham: 'Nganggur lagi, ya?'")
                    print(f"Stress +{ADDSTRESS[0]}")
                    stress += ADDSTRESS[0]
            else:
                if indekswaktu == "Pagi":
                    print("\nAlhaitham melihat kamu membuka sketsa di ruang kerja dan pergi tanpa bilang apa-apa.")
                    print("Stress -5")
                    terselesaikan = proyek.pop([0])
                    print(f"proyek {terselesaikan['nproyek']} terselesaikan!")
                    portofolio.append(terselesaikan)
                    stress -= 5
                    alhaitham_rew = True

            if indekswaktu == "Malam" and alhaitham_rew == True:
                print("\nAlhaitham memberikanmu secangkir kopi hangat.")
                print("Stress -20")
                stress -= 20
            return

        elif kegiatan == "2":
            if stress >= 75:
                print("Alhaitham melihat kamu yang kelelahan tidur. Ia pergi kerja tanpa bilang apa-apa.")
                stress -= 15
                print("Stress -15")
            else:
                print("Alhaitham melihat kamu kembali tidur dengan tatapan menghakimi.")
                stress += 5
                print("Stress +5")
            return

    else:
        print("Kamu sudah di rumah!")

def proyekan():
    if not proyek:
        print("\nproyek kosong. Ketik 'ljs' untuk cari kerja.")
    else:
        print("\nKaveh bekerja dengan rajin...")
        terselesaikan = proyek.pop(0)
        print(f"Proyek {terselesaikan['nproyek']} terselesaikan!")
        portofolio.append(terselesaikan)
        stress -= 15
        print(f"Stress -15")
        #Kegiatan selesai, pergantian jam
        indekswaktu = (indekswaktu + 1) % len(waktu)

#Intro game
print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh uang.")
print("Suatu hari, Kaveh dirasuki makhluk asing dari dunia lain.")
print(f"\nKetik 'lh' untuk melihat perintah")

#Main loop
while True:
    if hari <= 12 and stress < 100:
        print(f"\n[Hari ke-{hari}: {waktu[indekswaktu]}] [{uang} Mora] [{mood}]")
        print("Ketik 'lhelp' untuk menampilkan perintah.")
        perintah = input("\n> ")

        if perintah.strip().lower() == "lhelp":
            show_perintah()

        elif perintah.strip().lower() == "ld":
            detail()

        elif perintah.strip().lower() == "lw":
            tujuan = show_map()
            if hari != 1 and tujuan.strip().lower() == "1":
                walk_home()
            time_pass()

        elif perintah.strip().lower() == "ljs":
            job_search()

        elif perintah.strip().lower() == "lp":
            proyekan()
            time_pass()