# - login menu
# - Notifikasi projek ditawar/lamaran diterima
# Dokumentasi/tutorial/demo
# Rute tawar


data_user = {
    'admin': {
        'password' : 'admin123', 
        'dashboard': {
            'biodata' : {
                'nama':'Udin',
                'asal_instansi':'Universitas Mulawarman',
                'kontak':'@admin_123(ig)'
            },
            'projek_aktif' : {
                'penawaran' : None,
                'lamaran' : None
            },
            'portofolio' : None
        }
    }
}

lomba = {
    'pembuat_penawaran':'admin',
    'info':{
        'nama_lomba':None,
        'kategori':'Hackathon',
        'benefit':'200jt',
        'kriteria_pelamar':None,
        'link':None
    },
    'deskripsi':'Cantumkan gform in di lampiran yaa.',
    'lampiran':None,
    'pelamar_sekarang':None
}

def login():
    pass

def buat_penawaran():
    pass

def lamar_lomba():
    pass

def filter_penawaran():
    pass

def show_penawaran():
    filter_penawaran()
    penawaran = input("klik lomba.\n> ")
    lamar_lomba(penawaran)

def show_home():
    show_penawaran()

def show_halamanTawar():
    filter_penawaran()
    lamar_lomba()
    
def show_profile():
    pass

def edit_prfil():
    pass

def navigasi():
    pass
    # if pilihan == 1: show profile
    # elif pilihan == 2: buat penawaran()
    # elif pilihan == 3: show_halamanTawar()

def mulai_app():
    login()
    show_home()