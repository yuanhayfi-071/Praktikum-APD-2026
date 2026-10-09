#Settingan game
hari = 1
stress = 25 #Death flag: stress >= 100
uang = 100 #Objektif: bayar utang 1k Mora di hari ke-12

#Settingan waktu
waktu = ["Pagi","Siang","Sore","Malam"]
indekswaktu = 0

#Kerjaan
projek = []
waitlist = []
portofolio = []
pos_job = [1]

#Intro game
print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh uang.")
print("Ia punya utang 1k Mora yang harus dibayar 7 hari lagi!")
print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
print(f"\nKetik 'lh' untuk melihat perintah.")

while True: #Main loop
    if hari != 8:
        print(f"\n[Hari ke-{hari}: {waktu[indekswaktu]}] [{uang} Mora]")
        perintah = input("\n> ")

        if perintah.strip().lower() == "lh":
            print("\n=====Perintah=====")
            print("ld   -> Detail status" \
                "\nljs  -> Cari kerja" \
                "\nlp   -> Kerja")

        elif perintah.strip().lower() == "ld":
            print(f"\n=====DETAIL=====")
            if not projek:
                print("Projek: Kosong, masih nganggur!")
            else:
                for i, item in enumerate(projek, start=1):
                    print(f"{i}. Projek: {item['nprojek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")
            if not portofolio:
                print("Portofolio: Kosong, ayo kerja!")
            else:
                for i, item in enumerate(portofolio, start=1):
                    print(f"{i}. Portofolio: {item['nprojek']}")

        elif perintah.strip().lower() == "ljs":
            print(f"Melihat tawaran di papan pengumumam...")
            print(f"=====JOB LIST=====")
            print("1. Desain Rumah nyaman | 50 Mora | 3 hari")
            if len(portofolio) >= 3:
                pos_job.append(2,3)
                print("2. Desain Rumah Mewah | 125 Mora | 5 hari")
                print("3. Desain Toko Mewah | 100 Mora | 5 hari")

            while True: #Loop menambahkan kerja
                opsi = input("\nKetik 'ladd INDEKS' dipisahkan spasi untuk mengambil pekerjaan." \
                "\nAtau ketik 'lret' untuk keluar dari menu cari kerja.\n> ")
                bagian = opsi.lower().split()
                if bagian[0] == "lret":
                    print("Keluar dari menu cari kerja...")
                    break
                
                elif bagian[0] == "ladd" and all(x.isdigit() for x in bagian[1:len(bagian)]):
                    for x in bagian[1:len(bagian)]:
                        i = int(x)
                        if i not in pos_job:
                            print("Indeks tidak ditemukan.")
                            break
                        if i == "1":
                            waitlist.append({"nprojek":"Desain Rumah Nyaman","bayaran":50,"tenggat":3})
                        elif i == "2":
                            waitlist.append({"nprojek":"Desain Rumah Mewah","bayaran":125,"tenggat":5})
                        elif i == "3":
                            waitlist.append({"nprojek":"Desain Toko Mewah","bayaran":100,"tenggat":5})

                    print("\n")
                    if not waitlist:
                        print(f"Indeks tidak ditemukan.")
                        
                    for n, item in enumerate(waitlist, start=1):
                        print(f"{n}. {item['nprojek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")
                    
                    while True: #Loop konfirmasi
                        konfirmasi = input("Ketik 'confirm' atau 'cancel'.\n> ")
                        if konfirmasi.strip().lower() == "confirm":
                            print("\nDikonfirmasi! Silahkan cek detail anda.")
                            projek.append(waitlist)
                            break
                        elif konfirmasi.strip().lower() == "cancel":
                            print("Dibatalkan!")
                            break

        elif perintah.strip().lower() == "lp":
            if not projek:
                print("Projek: Kosong, masih nganggur!")
                continue

            for i, item in enumerate(projek, start=1):
                print(f"{i}. Projek: {item['nprojek']} | {item['bayaran']} | Tenggat: {item['tenggat']}")

            while True: #Loop utama Lp
                kerjakan = input("Pilih indeks projek untuk dikerjakan atau ketik 'cancel'.\n> ")
                if kerjakan == "cancel":
                    print("Batal mengerjakan...")
                    break
                try:
                    kerjakan = int(kerjakan)
                except ValueError:
                    print("Indeks projek tidak ditemukan!")
                    continue

                if kerjakan in range(1,len(projek)):
                    terselesaikan = projek.pop()
                    print(f"\nProjek {terselesaikan['nprojek']} selesai!")
                    print(f"Mora +{terselesaikan['bayaran']}")
                    portofolio.append(terselesaikan['nprojek'])
                    uang += terselesaikan['bayaran']

                    indekswaktu = (indekswaktu + 1) % len(waktu)
                    print(f"\nWaktu telah berlalu...\nSekarang [{waktu[indekswaktu]}]")
                    continue
    
    else: #Ending
        print("Hari ke-7 telah berlalu. Saatnya bayar utang.")
        if uang < 1000:
            print("Bad ending! Kaveh harus berlutut pada Alhaitham.")
        else:
            print("Good ending! Kaveh senang.")