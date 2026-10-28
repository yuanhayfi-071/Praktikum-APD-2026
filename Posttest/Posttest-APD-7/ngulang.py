import copy
import time
import os

PROJECT_FIELDS = {
    "nproyek": "Nama Proyek",
    "stresscost": "Stress",
    "bayaran": "Mora",
    "tenggat": "Tenggat"
}
all_project = [
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
    'waktu':{
        'Siang':{'restval':20, 'timestress':10},
        'Malam':{'restval':40, 'timestress':15}
    },
    'DEADLSTRESS' : 50
}

DEFAULT_PROGRESS = {
    'hari': 1,
    'mora' : 100,
    'stress' : 25,
    'indekswaktu':0,
    'proyek':[],
    'portofolio':[],
    'waitlist':[]
}

ENDINGS = {
    'stress_end': (
        "\nTingkat stress: {stress}"
        "\nKaveh jatuh dalam keterpurukan."
        "\nGAME OVER!"
    ),
    'good_end': (
        "\nHari ke-{batas_hari} telah berlalu. Saatnya bayar utang."
        "\nGood ending! Mora {mora}."
        "\nKaveh membayar utangnya pada Alhaitham."
    ),
    'bad_end': (
        "\nHari ke-{batas_hari} telah berlalu. Saatnya bayar utang."
        "\nBad ending! Mora {mora} kurang dari {utang_awal}."
        "\nKaveh harus berlutut pada Alhaitham!"
    )
}

def clear_terminal(x=1.5, m=None):
    if m is not None:
        print(m)
    time.sleep(x)
    os.system('cls' if os.name == 'nt' else 'clear') 

def ask_number(minimum=None, maximum=None, prompt="Ketik indeks atau 'kembali'.\n> "):
    while True:
        try:
            number = input(prompt).strip().lower()
            if number == 'kembali':
                return number
            if not number:
                raise ValueError('Angka tidak boleh kosong!')
            if not number.isdigit():
                raise ValueError('Input harus berupa angka.')

            number = int(number)
            if minimum is not None and number < minimum:
                raise ValueError(f'Angka minimal {minimum}.')
            if maximum is not None and number > maximum:
                raise ValueError(f'Angka maksimal {maximum}')
            return number
        except ValueError as e:
            print(e)
            return ask_number(minimum, maximum, prompt)
    
def waktu_sekarang(session):
    NAMA_WAKTU = list(SETTINGS['waktu'])
    try:
        return NAMA_WAKTU[session['progress']['indekswaktu']]
    except IndexError:
        session['progress']['indekswaktu'] = 0
        return NAMA_WAKTU[0]

def login_menu():
    while True:
        clear_terminal(1.5, "Membersihkan terminal...")
        print("="*5,"SIMULASI HIDUP KAVEH", "="*5)
        print("Silahkan masuk ke akun anda.")
        print("1. Sudah punya akun -> Log in")
        print("2. Belum punya akun -> Sign in")
        opsi = input("> ").strip()
        if opsi == '1':
            session = login()
            if session:
                return session
        elif opsi == '2':
            sign_up()
        else:
            print('\nOpsi tidak ditemukan.')

def login():
    clear_terminal(0, None)
    while True:
        print("="*5,"HALAMAN LOGIN","="*5)
        username = input('\nMasukkan nama pengguna atau ketik \'kembali\'.\n> ').strip().lower()
        if username == 'kembali':
            return None
        
        akun_ditemukan = data_user.get(username)
        if not akun_ditemukan:
            print('Akun tidak ditemukan!')
            continue
        
        password = input('Masukkan kata sandi.\n> ')
        if password == data_user[username]['password']:
            print('\nLogin berhasil!')
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
    print("="*5,"HALAMAN SIGN UP","="*5)
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
    clear_terminal(1.5, 'Memuat game...')
    print(f"BERMAIN DALAM MODE {session['access'].upper()}")
    print("\nKaveh adalah arsitek baik hati, emosional, idealis, dan butuh mora.")
    print(f"Ia punya utang {SETTINGS['utang_awal']} Mora yang harus dibayar {SETTINGS['batas_hari']} hari lagi!")
    print("Namun, Kaveh tiba-tiba dirasuki makhluk asing dari dunia lain...")
    print(f"\nHINT: Bekerja/istirahat menambah/mengurangi stress berbeda di (siang/malam)")  

def time_pass(session):
    session['progress']['indekswaktu'] = (session['progress']['indekswaktu'] + 1) % len(SETTINGS['waktu'])
    print(f"\nWaktu berlalu... Sekarang {waktu_sekarang(session)}.")
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
    clear_terminal(1.5, "Mengecek papan informasi...")
    while True:
        clear_terminal(0, None)
        print("\n+ \nTAWARAN PROYEK")
        for i, item in enumerate(all_project, start=1):
            print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
        print("+")
        opsi = input("\nKetik 'ladd' satu atau beberapa '[INDEX]' untuk mengambil kerjaan atau 'kembali'.\n> ").lower()
        bagian = opsi.split()
        if not bagian:
            continue
        elif bagian[0] == "kembali":
            clear_terminal(1.5, "Pergi dari papan informasi...")
            break
        elif bagian[0] == "ladd" and all(x.isdigit() for x in bagian[1:len(bagian)]):
            session['progress']['waitlist'].clear()
            for x in bagian[1:len(bagian)]:
                i = int(x)
                if 1 <= i <= len(all_project):
                    session['progress']['waitlist'].append(all_project[i-1].copy())
            if not session['progress']['waitlist']:
                print("Indeks tidak ditemukan!")
                continue
            else:
                clear_terminal(0, None)
                print("\nMemilih proyek:")
                session['progress']['waitlist'].sort(key=lambda k:k['nproyek'])
                for i, item in enumerate(session['progress']['waitlist'], start=1):
                    print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")
                while True:    
                    confirm = input("\nKetik 'confirm' untuk konfirmasi atau 'kembali'.\n> ")
                    if confirm.strip().lower() == 'confirm':
                        print("Dikonfirmasi!")
                        session['progress']['proyek'].extend(session['progress']['waitlist'])
                        break
                    elif confirm.strip().lower() == 'kembali':
                        print("\nDibatalkan!")
                        break
        else:
            print("Perintah tidak dikenali.")
        time.sleep(1.5)

def lp(session):
    clear_terminal(0, None)
    if not session['progress']['proyek']:
        print('Proyek kosong, masih nganggur!')
        input("Ketik apa saja untuk kembali.\n> ")
        clear_terminal(0, None)
        return
    for i, item in enumerate(session['progress']['proyek'], start=1):
        print(f"{i}. {item['nproyek']} | {item['bayaran']} Mora | Stress: {item['stresscost']} | Tenggat: {item['tenggat']}")
    opsi = input("\nKetik satu '[INDEX]' untuk dituntaskan atau 'kembali'.\n> ")
    if opsi.strip().lower() == "kembali":
        clear_terminal(0, "\nBatal bekerja...")
        return
    elif opsi.isdigit() and 1 <= int(opsi) <= len(session['progress']['proyek']):
        opsi = int(opsi)
        clear_terminal(1.5, "\nKaveh bekerja dengan rajin...")
        terselesaikan = session['progress']['proyek'].pop(opsi-1)
        session['progress']['portofolio'].append(terselesaikan)
        print(f"{terselesaikan['nproyek']} terselesaikan!")
        session['progress']['mora'] += terselesaikan['bayaran']
        print(f"Mora +{terselesaikan['bayaran']}")
        session['progress']['stress'] += SETTINGS['waktu'][waktu_sekarang(session)]['timestress'] + terselesaikan['stresscost']
        print(f"Stress +{(SETTINGS['waktu'][waktu_sekarang(session)]['timestress']) + terselesaikan['stresscost']}")
        time_pass(session)
    else:
        print("Indeks tidak ditemukan!")

def lr(session):
    clear_terminal(1.5, "Kaveh memilih tidur di rumah...")
    session['progress']['stress'] -= SETTINGS['waktu'][waktu_sekarang(session)]['restval']
    if session['progress']['stress'] < 0:
        session['progress']['stress'] = 0
    print(f"Stress -{SETTINGS['waktu'][waktu_sekarang(session)]['restval']}")
    print("Kaveh merasa segar kembali!")
    print(f"Tingkat stress: {session['progress']['stress']}")
    time_pass(session)

def edit_time():
    print('\nMengubah daftar waktu...')
    nama_waktu = input('Ketik nama waktu.\n> ').strip().title()
    try:
        data = SETTINGS['waktu'][nama_waktu]
    except KeyError:
        print(f"Waktu '{nama_waktu}' tidak ditemukan!")
        clear_terminal(1, None)
        return

    field = input('Ketik untuk mengubah nama, restval, atau timestress.\n> ').strip().lower()
    if field == 'nama':
        new_name = input(f"Mau ubah {nama_waktu} jadi apa?\n> ").strip().title()
        if not new_name:
            print("Nama tidak boleh kosong!")
        elif new_name in SETTINGS['waktu']:
            print(f"Waktu '{new_name}' sudah ada!")
        else:
            SETTINGS['waktu'] = {
                (new_name if k == nama_waktu else k): v
                for k, v in SETTINGS['waktu'].items()
            }
            print(f"Berhasil mengubah {nama_waktu} jadi {new_name}!")
    elif field in ('restval', 'timestress'):
        new_value = ask_number(0, None, "Ketik nilai atau 'kembali'.\n> ")
        if new_value == 'kembali':
            return
        data[field] = new_value
        print(f"Berhasil mengubah {field} {nama_waktu} jadi {new_value}!")
    else:
        print("Atribut tidak ditemukan!")
    clear_terminal(1, None)

def delete_time():
    print("\nMenghapus waktu dari daftar waktu...")
    nama_waktu = input('Ketik nama waktu.\n> ').strip().title()
    try:
        if len(SETTINGS['waktu']) <= 1:
            raise ValueError("Minimal harus ada satu waktu!")
        SETTINGS['waktu'].pop(nama_waktu)
    except KeyError:
        print(f"Waktu '{nama_waktu}' tidak ditemukan!")
    except ValueError as e:
        print(e)
    else:
        print(f"Berhasil menghapus {nama_waktu}!")
    clear_terminal(1.5, None)

def edit_value():
    clear_terminal(0, None)
    for index, (setting, value) in enumerate(SETTINGS.items(), start=1):
        print(f"{index}. {setting} | {value} ")
    print("\nPilih indeks pengaturan untuk diubah.")
    number = ask_number(1, len(SETTINGS), "Ketik indeks atau 'kembali'.\n> ")
    if number == 'kembali':
        return
    
    choosen_field = list(SETTINGS.keys())[number-1]
    if choosen_field == 'waktu':
        action = input("Ketik 'ubah' atau 'hapus' waktu.\n> ").strip().lower()
        if action == 'ubah':
            edit_time()
        elif action == 'hapus':
            delete_time()
        else:
            print('Perintah tidak dikenali.')
    
    else:
        print(f"\nMemilih mengubah {choosen_field}.")
        new_value = ask_number(0, None, "Masukkan nilai baru.\n> ")
        if new_value == 'kembali':
            return
        print(f'{choosen_field} telah diubah menjadi {new_value}')
        SETTINGS[choosen_field] = new_value
        clear_terminal(0, None)

def show_projects():
    for i, item in enumerate(all_project, start=1):
        print(f"{i}. {item['nproyek']} | Stress: {item['stresscost']} | {item['bayaran']} Mora | Tenggat: {item['tenggat']}")

def create_project():
    list_field = list(PROJECT_FIELDS)
    project_baru = {}
    for field in list_field:
        if field == 'nproyek':
            nama = input("Input nama proyek.\n> ")
            project_baru.update({'nproyek':nama})
            continue
        nilai = ask_number(1, None, f"\nInput {PROJECT_FIELDS[field]}.\n> ")
        project_baru.update({field:nilai})

    all_project.append(project_baru)
    print(f"Proyek'{project_baru}' berhasil dibuat!")

def edit_project_field():
    clear_terminal(0, None)
    show_projects()
    indeks = ask_number(1, len(all_project), 'Pilih indeks proyek atau \'kembali\'.\n> ')
    if indeks == 'kembali':
        clear_terminal(0, None)
        return
    project = all_project[indeks - 1]

    daftar = list(PROJECT_FIELDS)
    print()
    for i, field in enumerate(daftar, start=1):
        print(f"{i}. {PROJECT_FIELDS[field]}")
    pilihan = ask_number(1, len(daftar), 'Pilih atribut atau \'kembali\'.\n> ')
    if pilihan == 'kembali':
        clear_terminal(0, None)
        return
    field = daftar[pilihan - 1]

    if field == 'nproyek':
        nilai = input(f"\nMasukkan nama baru untuk \'{project['nproyek']}\'.\n> ").strip()
        if not nilai:
            print('Nama proyek tidak boleh kosong!')
            return
    else:
        nilai = ask_number(1, None, f"\nMasukkan nilai baru untuk {PROJECT_FIELDS[field]} atau 'kembali'.\n> ")
        if nilai == 'kembali':
            return

    lama = project[field]
    project[field] = nilai
    print(f"\nMengubah {PROJECT_FIELDS[field]} dari {lama} menjadi {nilai}.")

def edit_project():
    while True:
        pilihan = input("\nKetik 'lnew' membuat proyek baru, 'ledp' mengedit, atau 'kembali'.\n> ").strip().lower()
        if pilihan == 'kembali':
            break
        elif pilihan == 'lnew':
            create_project()
        elif pilihan == 'ledp':
            edit_project_field()
        else:
            print("Perintah tidak dikenali.")

def led():
    clear_terminal(0, None)
    print("\nEDIT SISTEM\n1. Pengaturan\n2. Proyek")
    pilihan = ask_number(1, 2)
    if pilihan == 1:
        edit_value()
    elif pilihan == 2:
        edit_project()

def show_users():
    print("\nDAFTAR PENGGUNA")
    for i, (nama, akun) in enumerate(data_user.items(), start=1):
        print(f"{i}. {nama} | Akses: {akun['access']}")

def ask_username(prompt, session):
    nama = input(f"\n{prompt} atau 'kembali'.\n> ").strip().lower()
    if nama == 'kembali':
        return None
    if nama not in data_user:
        print("Akun tidak ditemukan.")
        return None
    if nama == session['username']:
        print("Tidak bisa mengedit akun yang sedang digunakan.")
        return None
    return nama

def change_access(session):
    nama = ask_username("Ketik nama akun untuk diubah aksesnya", session)
    if nama is None:
        return
    baru = input("\nKetik 'admin' atau 'member'.\n> ").strip().lower()
    if baru not in ('admin', 'member'):
        print(f"Akses {baru} tidak ditemukan.")
    elif data_user[nama]['access'] == baru:
        print(f"Akses {nama} sudah {baru}.")
    else:
        data_user[nama]['access'] = baru
        print(f"Akses {nama} diubah menjadi {baru}.")

def delete_user(session):
    nama = ask_username("Ketik nama akun yang ingin dihapus", session)
    if nama is None:
        return
    while True:
        konfirmasi = input(f"\nKetik 'confirm' untuk menghapus {nama} atau 'kembali'.\n> ").strip().lower()
        if konfirmasi == 'confirm':
            del data_user[nama]
            print(f"Pengguna {nama} dihapus!")
            return
        elif konfirmasi == 'kembali':
            return

def lusd(session):
    while True:
        clear_terminal(0, None)
        show_users()
        pilihan = input("\nKetik 'lacs' untuk mengubah akses, 'lrem' untuk menghapus akun, atau 'kembali'.\n> ").strip().lower()
        if pilihan == 'kembali':
            clear_terminal(0, None)
            return
        elif pilihan == 'lacs':
            change_access(session)
        elif pilihan == 'lrem':
            delete_user(session)
        else:
            print("Perintah tidak ditemukan.")
        time.sleep(1.5)

def game_loop(session):
    while True:
        ending = check_ending(session)
        if ending:
            show_ending(ending, session)
            input("Ketik apapun untuk kembali ke halaman login.\n> ")
            return
        
        print(f"\nKetik 'lh' untuk melihat perintah atau 'kembali' ke halaman login.")
        print(f"[Hari ke-{session['progress']['hari']}/{SETTINGS['batas_hari']}: {waktu_sekarang(session)}] [{session['progress']['mora']}/{SETTINGS['utang_awal']} Mora]")
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
        elif perintah == 'lr':
            lr(session)
        elif session['access'] == 'admin':
            if perintah == 'led':
                led()
            elif perintah == 'lusd':
                lusd(session)
        else:
            print("Perintah tidak ditemukan.")

def check_ending(session):
    if session['progress']['stress'] >= SETTINGS['batas_stress']:
        return 'stress_end'
    if session['progress']['hari'] > SETTINGS['batas_hari'] and session['progress']['mora'] >= SETTINGS['utang_awal']:
        return 'good_end'
    if session['progress']['hari'] > SETTINGS['batas_hari'] and session['progress']['mora'] < SETTINGS['utang_awal']:
        return 'bad_end'
    return None

def show_ending(ending, session):
    clear_terminal(0, None)
    print(ENDINGS[ending].format(
        stress=session['progress']['stress'],
        mora=session['progress']['mora'],
        utang_awal=SETTINGS['utang_awal'],
        batas_hari=SETTINGS['batas_hari'] - 1,
    ))

def run_game():
    session = login_menu()
    if not session:
        return
    intro(session)
    hasil = game_loop(session)
    if hasil == 'kembali':
        return
    
while True:
    run_game()