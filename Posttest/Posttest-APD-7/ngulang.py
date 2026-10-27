import copy
import time
import os

all_job = [
    {"nproyek":"Desain Rumah Nyaman","stresscost":5,"bayaran":50,"tenggat":2},
    {"nproyek":"Desain Rumah Mewah","stresscost":15,"bayaran":125,"tenggat":3}, 
    {"nproyek":"Desain Toko Mewah","stresscost":10,"bayaran":115,"tenggat":3}
]

data_user = {
    'admin':{
        'password':'admin123', 
        'access':'admin', 
        'progress':None
    }
}

session = {'user': None, 'access': None, 'progress':None}

SETTINGS = {
    'batas_hari': 7,
    'utang_awal': 1000,
    'batas_stress': 100,
    'waktu':['Siang','Malam'],
    'RESTVAL' : [20, 40],
    'TIMESTRESSVAL' : [10, 15],
    'DEADLSTRESS' : 50
}

DEFAULT_PROGRESS = {
    'hari': 1,
    'mora' : 100,
    'stress' : 25,
    'indekswaktu':0,
    'proyek':[],
    'portofolio':[],
    'waitlist':[],
    'pos_job':[all_job[0]],
}

def clear_terminal(x, m):
    if m == 'def':
        print('Membersihkan terminal...')
    elif m == 'ljs':
        print('Mengecek papan informasi...')
    elif m == 'lp':
        print('Kaveh bekerja dengan rajin...')
    elif m == 'lr':
        print('Kaveh memilih untuk tidur...')
    time.sleep(x)
    os.system('cls' if os.name == 'nt' else 'clear') 

def login_menu():
    clear_terminal(1.5, None)
    while True:
        print('Pilih cara masuk.\n1. Login \n2. Sign up')
        opsi = input("> ").strip()
        if opsi == '1':
            session = login()
            if session:
                return session
        elif opsi == '2':
            sign_up()
        else:
            print('Opsi tidak ditemukan.')

def login():
    clear_terminal(0, None)
    while True:
        username = input('\nMasukkan nama pengguna atau ketik \'kembali\'.\n> ').strip().lower()
        if username == 'kembali':
            return None
        
        akun_ditemukan = data_user.get(username)
        if not akun_ditemukan:
            print('Akun tidak ditemukan!')
            continue
        
        password = input('\nMasukkan kata sandi.\n> ')
        if password == data_user[username]['password']:
            print('Login berhasil!')
            if data_user[username]['progress'] is None:
                data_user[username]['progress'] = new_progress()

            session = {
                'username':username,
                'access': data_user[username]['access'],
                'progress': data_user[username]['progress']
            }
            return session
        else:
            print('Kata sandi salah!')

def sign_up():
    clear_terminal(0, None)
    username = input("\nMasukkan nama pengguna baru atau '/kembali'.\n> ").strip().lower()
    usn_exist = data_user.get(username)
    if username == "/kembali":
        return
    elif len(username.strip()) == 0:
        print("Nama pengguna tidak boleh kosong.")
    elif usn_exist:
        print(f"Nama pengguna {username} sudah ada.")
    else:
        password = input("Masukkan password baru.\n> ")
        data_user[username] = {
            'password': password,
            'access': 'member',
            'progress': new_progress()
        }
        print(f"\nAkun {username} berhasil dibuat!")

def new_progress():
    return copy.deepcopy(DEFAULT_PROGRESS)

def intro(session):
    clear_terminal(1.5, 'def')
    print(f"BERMAIN DALAM MODE {session['access'].upper()}")
    print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
    print(f"Ia punya utang {SETTINGS['utang_awal']} Mora yang harus dibayar {SETTINGS['batas_hari']+1} hari lagi!")
    print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
    print(f"\nHINT: Bekerja menambah stress ({SETTINGS['TIMESTRESSVAL'][0]}/{SETTINGS['TIMESTRESSVAL'][1]}) di (siang/malam), "
    f"sedangkan Beristirahat mengurangi ({SETTINGS['RESTVAL'][0]}/{SETTINGS['RESTVAL'][1]}) di (siang/malam).")  

def time_pass(session):
    session['progress']['indekswaktu'] = (session['progress']['indekswaktu'] + 1) % len(SETTINGS['waktu'])
    print(f"\nWaktu berlalu... Sekarang {SETTINGS['waktu'][session['progress']['indekswaktu']]}.")
    if session['progress']['indekswaktu'] == 0:
        print("Sehari terlewati...")
        session['progress']['hari'] += 1
        sisa = [] #Menampung proyek2 yg tenggatnya blm habis saat disaring
        for i, item in enumerate(session['progress']['proyek']):
            item['tenggat'] -= 1
            if item['tenggat'] <= 0:
                session['progress']['stress'] += SETTINGS['DEADLSTRESS']
                print(f"Tenggat {item['nproyek']} terlewat! Stress +{SETTINGS['DEADLSTRESS']}")
            else:
                sisa.append(item)
        session['progress']['proyek'][:] = sisa
    if session['progress']['stress'] >= SETTINGS['batas_stress'] or session['progress']['hari'] >= SETTINGS['batas_hari']:
        return

def lh(session):
    clear_terminal(0, None)
    print("\n+ \nPERINTAH")
    print("ld   -> Detail status" \
        "\nljs  -> Cari kerja" \
        "\nlp   -> Kerja"
        "\nlr   -> Istirahat")
    if session['access'] == 'admin':
        print("led   -> Edit Sistem/Atribut" \
        "\nlusd  -> Edit Data User")
    print("+")

def ld(session):
    clear_terminal(0, None)
    print("\n+ \nDETAIL STATUS")
    print(f"Mora: {session['progress']['mora']}")
    print(f"Stress: {session['progress']['stress']}")

    if not session['progress']['proyek']:
        print("\nProyek kosong, masih nganggur!")
    else:
        print(f"\nProyek:")
        for i, item in enumerate(session['progress']['proyek'], start=1):
            print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora | Stress: {item['stresscost']} | Tenggat: {item['tenggat']}")  

    if not session['progress']['portofolio']:
        print(f"\nPortofolio kosong, ayo kerja!")
    else:
        print(f"\nPortofolio:")
        for i, item in enumerate(session['progress']['portofolio'], start=1):
            print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora")
    print("+")

def ljs(session):
    clear_terminal(1.5, 'ljs')
    while True:
        clear_terminal(0, None)
        print("\n+ \nTAWARAN PROYEK")
        for i, item in enumerate(session['progress']['pos_job'], start=1):
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
            session['progress']['waitlist'].clear()
            for x in bagian[1:len(bagian)]:
                i = int(x)
                if 1 <= i <= len(session['progress']['pos_job']):
                    session['progress']['waitlist'].append(session['progress']['pos_job'][i-1].copy())
            if not session['progress']['waitlist']:
                print("Indeks tidak ditemukan!")
                continue
            else:
                os.system('cls')
                print("\nMemilih proyek:")
                session['progress']['waitlist'].sort(key=lambda k:k['nproyek'])
                for i, item in enumerate(session['progress']['waitlist'], start=1):
                    print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                while True:    
                    confirm = input("\nKetik 'confirm' untuk konfirmasi atau 'kembali'.\n> ")
                    if confirm.strip().lower() == 'confirm':
                        print("\nDikonfirmasi!")
                        session['progress']['proyek'].extend(session['progress']['waitlist'])
                        break
                    elif confirm.strip().lower() == 'kembali':
                        print("\nDibatalkan!")
                        break
        else:
            print("Perintah tidak dikenali.")
        time.sleep(1.5)

def lp(session):
    if not session['progress']['proyek']:
        print('Proyek kosong, masih nganggur!')
        return
    opsi = input("\nKetik satu '[INDEX]' untuk dituntaskan atau 'kembali'.\n> ")
    if opsi.strip().lower() == "kembali":
        print("Batal bekerja...")
        return opsi
    elif opsi.isdigit() and 1 <= int(opsi) <= len(session['progress']['proyek']):
        opsi = int(opsi)
        print("Kaveh bekerja dengan rajin...")
        time.sleep(1.5)
        os.system('cls')
        terselesaikan = session['progress']['proyek'].pop(opsi-1)
        session['progress']['portofolio'].append(terselesaikan)
        print(f"{terselesaikan['nproyek']} terselesaikan!")
        session['progress']['mora'] += terselesaikan['bayaran']
        print(f"Mora +{terselesaikan['bayaran']}")
        session['progress']['stress'] += SETTINGS['TIMESTRESSVAL'][session['progress']['indekswaktu']] + terselesaikan['stresscost']
        print(f"Stress +{(SETTINGS['TIMESTRESSVAL'][session['progress']['indekswaktu']]) + terselesaikan['stresscost']}")
        time_pass(session)
    else:
        print("Indeks tidak ditemukan!")

def led(p):
    pass

def lusd(p):
    pass

def game_navigation(session):
    print(f"\nKetik 'lh' untuk melihat perintah atau 'kembali' ke halaman login.")
    print(f"[Hari ke-{session['progress']['hari']}/{SETTINGS['batas_hari']}: {SETTINGS['waktu'][session['progress']['indekswaktu']]}] [{session['progress']['mora']}/{SETTINGS['utang_awal']} Mora]")
    perintah = input("> ")
    if perintah == 'kembali':
        return 'kembali'
    elif perintah == 'lh':
        lh(session)
    elif perintah == 'ld':
        ld(session)
    elif perintah == 'ljs':
        ljs(session)
    elif perintah == 'lp':
        lp(session)
    elif session['access'] == 'admin':
        if perintah == 'led':
            led(session)
        elif perintah == 'lusd':
            lusd(session)
    else:
        print("Perintah tidak ditemukan.")

def run_game():
    session = login_menu()
    if not session:
        return
    intro(session)
    while session['progress']['hari'] <= SETTINGS['batas_hari'] and session['progress']['stress'] < SETTINGS['batas_stress']:
        hasil = game_navigation(session)
        if hasil == 'kembali':
            break

while True:
    run_game()