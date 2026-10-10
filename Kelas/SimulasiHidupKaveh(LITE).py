#Settingan game
hari = 1
stress = 25 #Death flag: stress >= 100
mora = 100 #Objektif: bayar utang 1k Mora di hari ke-8
RESTVAL = [20, 40]
TIMESTRESSVAL = [10, 15]
DEADLSTRESS = 50

#Settingan waktu
waktu = ["Siang","Malam"]
indekswaktu = 0

#Kerjaan
proyek = []
portofolio = []
waitlist = []
pos_job = [{"nproyek":"Desain Rumah Nyaman","stresscost":5,"bayaran":50,"tenggat":2}]

#Intro game
print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
print("Ia punya utang 1k Mora yang harus dibayar 7 hari lagi!")
print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
print(f"HINT: Bekerja menambah stress ({TIMESTRESSVAL[0]}/{TIMESTRESSVAL[1]}) di (siang/malam),"
      f"sedangkan Beristirahat mengurangi ({RESTVAL[0]}/{RESTVAL[1]}) di (siang/malam).")
print(f"Ketik 'lh' untuk melihat perintah.")

while True: #Main loop
    if len(pos_job) == 1 and len(portofolio) >= 3: #Kontrol porto
        pos_job.extend([
            {"nproyek":"Desain Rumah Mewah","stresscost":15,"bayaran":125,"tenggat":3}, 
            {"nproyek":"Desain Toko Mewah","stresscost":10,"bayaran":115,"tenggat":3}
            ])
        
    if hari < 8 and stress < 100: #Kontrol game
        print(f"\n[Hari ke-{hari}: {waktu[indekswaktu]}] [{mora}/1000 Mora]")
        perintah = input("\n> ")

        if perintah.strip().lower() == "lh":
            print("\n+ \nPERINTAH")
            print("ld   -> Detail status" \
                "\nljs  -> Cari kerja" \
                "\nlp   -> Kerja"
                "\nlr   -> Istirahat")
            print("+")

        elif perintah.strip().lower() == "ld":
            print("\n+ \nDETAIL STATUS")
            print(f"Stress: {stress}")
            if not proyek:
                print(f"\nProyek kosong, masih nganggur!")
            else:
                print(f"\nProyek:")
                for i, item in enumerate(proyek, start=1):
                    print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
            if not portofolio:
                print(f"Portofolio kosong, ayo kerja!")
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

            print("Kaveh merasa segar kembali!")
            print(f"Tingkat stress: {stress}")

    elif stress >= 100: #Death flag
        print("\nKaveh jatuh dalam keterpurukan.")
        print("GAME OVER!")
        break
    
    elif hari == 8: #Ending
        print("\nHari ke-7 telah berlalu. Saatnya bayar utang.")
        if mora < 1000:
            print(f"Bad ending! Mora {mora} kurang dari 1000.") 
            print(f"Kaveh harus berlutut pada Alhaitham!")
        else:
            print(f"Good ending! Mora {mora}. Kaveh membayar utangnya pada Alhaitham.")
        break