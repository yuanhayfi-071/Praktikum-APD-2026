#Settingan game
hari = 1
stress = 25 #Death flag: stress >= 100
mora = 100 #Objektif: bayar utang 1k Mora di hari ke-12

#Settingan waktu
waktu = ["Pagi","Siang","Sore","Malam"]
indekswaktu = 0

#Kerjaan
proyek = []
portofolio = []
waitlist = []
pos_job = [{"nproyek":"Desain Rumah Nyaman","bayaran":50,"tenggat":3}]

#Intro game
print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
print("Ia punya utang 1k Mora yang harus dibayar 7 hari lagi!")
print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
print(f"\nKetik 'lh' untuk melihat perintah.")

while True: #Main loop
    if len(pos_job) == 1 and len(portofolio) >= 3: #Kontrol porto
        pos_job.extend([
            {"nproyek":"Desain Rumah Mewah","bayaran":125,"tenggat":5}, 
            {"nproyek":"Desain Toko Mewah","bayaran":100,"tenggat":5}
            ])
        
    if hari < 8: #Kontrol menu
        print(f"\n[Hari ke-{hari}: {waktu[indekswaktu]}] [{mora} Mora]")
        perintah = input("\n> ")

        if perintah.strip().lower() == "lh":
            print("\n+ \nPERINTAH")
            print("ld   -> Detail status" \
                "\nljs  -> Cari kerja" \
                "\nlp   -> Kerja")
            print("+")

        elif perintah.strip().lower() == "ld":
            print("\n+ \nDETAIL STATUS")
            print(f"Stress: {stress}")
            if not proyek:
                print(f"Proyek kosong, masih nganggur!")
            else:
                print(f"Proyek:")
                for i, item in enumerate(proyek, start=1):
                    print(f"{i}. {item['nproyek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")
            if not portofolio:
                print(f"Portofolio kosong, ayo kerja!")
            else:
                print(f"Portofolio:")
                for i, item in enumerate(portofolio, start=1):
                    print(f"{i}. {item['nproyek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")
            print("+")

        elif perintah.strip().lower() == "ljs":
            print("\nMengecek papan informasi...")
            print("\n+ \nTAWARAN PROYEK")
            for i, item in enumerate(pos_job, start=1):
                print(f"{i}. {item['nproyek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")

            while True: #Mengambil kerja
                opsi = input("\nKetik 'ladd' satu atau beberapa '[INDEX]' untuk mengambil kerjaan atau 'cancel'.\n> ").lower()
                bagian = opsi.split()
                if not bagian:
                    continue
                elif bagian[0] == "cancel":
                    print("\nPergi dari papan informasi...")
                    break
                elif bagian[0] == "ladd" and all(x.isdigit() for x in bagian[1:len(bagian)]):
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
                            print(f"{i}. {item['nproyek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")
                        confirm = input("\nKetik 'confirm' untuk konfirmasi atau 'cancel'.\n> ")
                        if confirm.strip().lower() == 'confirm':
                            print("\nDikonfirmasi!")
                            proyek.extend(waitlist)
                            waitlist.clear()
                        elif confirm.strip().lower() == 'cancel':
                            print("\nDibatalkan!")
                            waitlist.clear()

        elif perintah.strip().lower() == "lp":
                while True:
                    if not proyek:
                        print("\nProyek kosong, masih nganggur!")
                        break
                    else:
                        print(f"\nProyek:")
                        for i, item in enumerate(proyek, start=1):
                            print(f"{i}. {item['nproyek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")
                                        
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

                                indekswaktu = (indekswaktu + 1) % len(waktu)
                                print("\nWaktu berlalu...")
                                if indekswaktu == 0:
                                    hari += 1
                                    for item in proyek:
                                        item['tenggat'] -= 1
                                    print("Sehari terlewati...")
                            else:
                                print("Indeks tidak ditemukan!")
                        else:
                            print("Indeks harus berupa satu angka!")
    
    else:
        print("Hari ke-7 telah berlalu. Saatnya bayar utang.")
        if mora < 1000:
            print("Bad ending! Kaveh harus berlutut pada Alhaitham.")
        else:
            print("Good ending! Kaveh membayar utangnya pada Alhaitham.")
        break