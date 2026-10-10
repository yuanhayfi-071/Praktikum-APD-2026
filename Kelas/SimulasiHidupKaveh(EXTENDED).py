#Settingan game
hari = 1
lokasi = "Rumah"
stress = 25
uang = 100

#Settingan waktu
waktu = ["Pagi","Siang","Sore","Malam"]
indekswaktu = 0

#Kerjaan
projek = []
portofolio = []

#Detail status
mood = "Netral" #: sedih, ceroboh & tidak efisiesn; senang, kreatif & efisien
status = [] #: mabuk, rawan dijambret; dikutuk, ;diberkati
karma = 0 # <25, bepergian bisa dapat mora, nyari kerja lancar; >50, bepergian malam bisa dijambret

#Intro game
print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh uang.")
print("Suatu hari, Kaveh dirasuki makhluk asing dari dunia lain.")
print(f"\nKetik 'lh' untuk melihat opsi")

#Main loop
while True:
    print(f"\n[Hari ke-{hari}: {waktu[indekswaktu]}] [{uang} Mora] [{mood}]")
    opsi = input("\n> ")

    if opsi.strip().lower() == "lh":
        print("\n=====OPSI=====")
        print("ld -> Detail status" \
                "\nlw -> Jalan" \
                "\nljs -> Cari kerja" \
                "\nlp -> Kerja")

    elif opsi.strip().lower() == "ld":
        print(f"\n=====DETAIL====="
              f"\nStatus = {status}"
              f"\nMood = {mood}"
              f"\nKarma = {karma}")
        if not projek:
            print("Projek = Kosong, masih nganggur")
        else:
            for i, daftar in enumerate(projek, start=1):
                print(f"{i}. Projek: {daftar['nprojek']} | Tenggat: {daftar['tenggat']}")

    elif opsi.strip().lower() == "lw":
        print("\n===LOKASI===")
        print("1. Rumah" \
        "\n2. Tavern" \
        "\n3. Akademiya" \
        "\n4. Grand Bazaar" \
        "\n5. Gandhara Vile" \
        "\n6. Aaru Village" \
        "\n7. Port Ormos")
        tujuan = input("\nPilih indeks lokasi.\n> ")

        if hari != 1 and tujuan.strip().lower() == "1":
            if lokasi != "Rumah":
                lokasi = "Rumah"
                print("Mau ngapain di rumah?")
                print("1. Menyibukkan diri"
                "\n2. Tidur")
                if indekswaktu == "Sore":
                    print("\n3. Ganggu Alhaitham")
                kegiatan = input("\n> ")

                if kegiatan == "1":
                    if len(projek) == 0:
                        if indekswaktu == "Pagi":
                            print("\nAlhaitham: 'Nganggur, ya?'")
                            print("Stress +5")
                            stress += 5
                        elif indekswaktu == "Sore":
                            print("\nAlhaitham yang baru pulang kerja mendapati kamu sedang lap lemari.")
                            print("Alhaitham: 'Nganggur lagi, ya?'")
                            print("Stress +5")
                            stress += 5
                    else:
                        if indekswaktu == "Pagi":
                            print("\nAlhaitham melihat kamu membuka sketsa di ruang kerja dan pergi tanpa bilang apa-apa.")
                            print("Stress -5")
                            terselesaikan = projek.pop([0])
                            print(f"Projek {terselesaikan['nprojek']} terselesaikan!")
                            portofolio.append(terselesaikan)
                            stress -= 5
                            alhaitham_rew = True

                    if indekswaktu == "Malam" and alhaitham_rew == True:
                        print("\nAlhaitham memberikanmu secangkir kopi hangat.")
                        print("Stress -20")
                        stress -= 20

                    #Kegiatan selesai, pergantian jam
                    indekswaktu = (indekswaktu + 1) % len(waktu)

                elif kegiatan == "2":
                    if stress >= 75:
                        print("Alhaitham melihat kamu yang kelelahan tidur. Ia pergi kerja tanpa bilang apa-apa.")
                        stress -= 15
                        print("Stress -15")
                    else:
                        print("Alhaitham melihat kamu kembali tidur dengan tatapan menghakimi.")
                        stress += 5
                        print("Stress +5")

            else:
                print("Kamu sudah di rumah!")

    elif opsi.strip().lower() == "ljs":
        print("\n=====MENCARI KERJA=====")
        print("1. Pasang brosur")
        print("2. Datangi Dori si pengusaha (agak kikir)")
        print("3. Datangi Nahida sang dewi")
        metode = input("\n> ")

        if metode == "1":
            if len(portofolio) <= 3:
                tambahkan = {"nprojek":"Desain Interior Biasa","tenggat":3,"progress":0}
                projek.append(tambahkan)
                print(f"\nProjek '{tambahkan['nprojek']}' didapat!")
            else:
                projek.append({"nprojek":"Desain Interior Mahal","tenggat":5,"prgress":0})

        #Kegiatan selesai, pergantian jam
        indekswaktu = (indekswaktu + 1) % len(waktu)

    elif opsi.strip().lower() == "lp":
        if not projek:
            print("\nProjek kosong. Ketik 'ljs' untuk cari kerja.")
        else:
            print("\nKaveh bekerja dengan rajin...")
            terselesaikan = projek.pop(0)
            print(f"Projek {terselesaikan['nprojek']} terselesaikan!")
            portofolio.append(terselesaikan)
            stress -= 15
            print(f"Stress -15")
            #Kegiatan selesai, pergantian jam
            indekswaktu = (indekswaktu + 1) % len(waktu)

    if hari != 1 and indekswaktu == 0:
        hari += 1
        print("\nSehari telah berlalu!")