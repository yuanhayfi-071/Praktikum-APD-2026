import copy

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

session = {'user': None}

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
    'proyek_aktif':[],
    'waitlist':[],
    'pos_job':[all_job[0]],
}

def login_menu():
    print('Pilih cara masuk.\n1. Login \n2. Sign up')
    opsi = print("Opsi login.\n> ")
    if opsi == '1':
        p = login()
    elif opsi == '2':
        sign_up()
    else:
        print('Opsi tidak ditemukan.')
    return p

def login():
    username = input('Type username.\n> ')
    akun_ditemukan = data_user.get(username)
    if not akun_ditemukan:
        print('Akun tidak ditemukan!')
    else:
        password = input('\nType password.\n> ')
        if password == data_user[username]['password']:
            print('Login berhasil!')
            session['user'] = username
    p = data_user[session['user']]['progress']
    return p

def sign_up():
    username = input("\nMasukkan nama pengguna baru atau '/kembali'.\n> ").strip().lower()
    usn_exist = data_user.get(username)
    if username == "/kembali":
        print("Membersihkan terminal...")
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
        print("Membersihkan terminal...")

def new_progress():
    return copy.deepcopy(DEFAULT_PROGRESS)

def intro(p):
    print(f"BERMAIN DALAM MODE {p['access'].upper()}")
    print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
    print(f"Ia punya utang {SETTINGS['utang']} Mora yang harus dibayar {SETTINGS['batas_hari']+1} hari lagi!")
    print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
    print(f"\nHINT: Bekerja menambah stress ({SETTINGS['TIMESTRESSVAL'][0]}/{SETTINGS['TIMESTRESSVAL'][1]}) di (siang/malam), "
    f"sedangkan Beristirahat mengurangi ({SETTINGS['RESTVAL'][0]}/{SETTINGS['RESTVAL'][1]}) di (siang/malam).")  

def show_activeproject(p):

def lh(p):
    print("\n+ \nPERINTAH")
    print("ld   -> Detail status" \
        "\nljs  -> Cari kerja" \
        "\nlp   -> Kerja"
        "\nlr   -> Istirahat")
    if p['access'] == 'admin':
        print("led   -> Edit Sistem/Atribut" \
        "\nlusd  -> Edit Data User")
    print("+")

def ld(p):
    print("\n+ \nDETAIL STATUS")
    print(f"Mora: {p['mora']}")
    print(f"Stress: {p['stress']}")
    show_activeproject(p)
    if not player['portofolio']:
        print(f"\nPortofolio kosong, ayo kerja!")
    else:
        print(f"\nPortofolio:")
        for i, item in enumerate(player['portofolio'], start=1):
            print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora")
    print("+")

def game_navigation(p):
    print(f"\nKetik 'lh' untuk melihat perintah atau 'kembali' ke halaman login.")
    print(f"[Hari ke-{p['hari']}/{SETTINGS['bhari']}: {SETTINGS['waktu'][p['indekswaktu']]}] [{p['mora']}/{SETTINGS['utang']} Mora]")
    perintah = input("> ")
    if perintah == 'lh':
        lh()
    elif perintah == 'ld':
        ld()

def run_game():
    p = login_menu()
    if not p:
        return
    else:
        intro(p)
        while p['hari'] <= SETTINGS['batas_hari'] and p['stress'] < SETTINGS['batas_stress']:
            while True:
                game_navigation(p)

while True:
    run_game()