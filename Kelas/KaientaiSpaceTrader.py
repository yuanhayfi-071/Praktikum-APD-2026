# Setting karakter
player = {"visa":0,"money":1000000,"cur_planet":"O-Edo",
          "warehouse":{
              "Fuel": {"amount":25}
              }
}

# Setting game
items = {
    "Fuel": {"base_price":50},
    "Plant": {"base_price":20},
    "Tobacco": {"base_price":30}
}

planets = {
    "O-Edo":{
        "rate":1,
        "stock":["Fuel","Plant"],
        "mod_price":{"Fuel":1.5, "Plant":0.8, "Tobacco":1} # Angka kecil = bagus beli, and vice versa.
    },

    "Hamek":{
        "rate":0.5, 
        "stock":["Tobacco"], 
        "mod_price":{"Fuel":0.5, "Plant":1.2, "Tobacco":0.8}
    },
}

# Mekanik game
def travel(player):
    planetnames = list(planets)
    print("\nDESTINASI")
    for i, name in enumerate(planetnames, start=1):
        print(f"{i}. {name}")
    destination = int(input("Ketik [INDEKS] destinasi.\n> "))
    if player['cur_planet'] != planetnames[destination-1]:
        player['cur_planet'] = planetnames[destination-1]
        print(f"Berangkat ke {player['cur_planet']}...")
    else: 
        print(f"Sudah berada di {player['cur_planet']}!")

def mto_local(amount, player): # Hitung base dalam local rate (kyknya bakal dipake buat uang lu doang)
    return amount / planets[player['cur_planet']]["rate"]

def mto_base(amount, player): # Hitung local price dalam base 
    return amount * planets[player['cur_planet']]["rate"]

def get_price(item, player): # Hitung local price
    return items[item]["base_price"] * planets[player['cur_planet']]["mod_price"][item]

def buying(player, local_price):
    price_inbase = mto_base(local_price, player)
    if player['money'] >= price_inbase:
        player['money'] -= price_inbase
        print("\nBerhasil membeli!")
        print(f"Uang: {player['money']}")
    else:
        print("Uang tidak cukup!")

def selling(player, local_price):
    price_inbase = mto_base(local_price, player)
    player['money'] += price_inbase
    print("\nBerhasil menjual!")
    print(f"Uang: {player['money']}")

def show_window(player):
    print(f"\nSTOK CARGO KAIENTAI CO.")
    for i, item in enumerate(player['warehouse'],start=1):
        local_price = get_price(item, player)
        print(f"{i}. {item}, local cost: {local_price} / base cost: {mto_base(local_price, player)}")

    print(f"\nSTOK PLANET {player['cur_planet'].upper()}")
    for i, item in enumerate(planets[player['cur_planet']]["stock"], start=1):
        local_price = get_price(item, player)
        print(f"{i}. {item}, local cost: {local_price} / base cost: {mto_base(local_price, player)}")

def openshop_andpick(player):
    show_window(player)
    option = input("\nKetik beli atau jual.\n> ")
    if option == "beli":
        avail_stock = planets[player['cur_planet']]["stock"]
        pick = int(input("Ketik [INDEX] barang.\n> "))
        # bikin bulk buying (bagian.split())
        if 1 <= pick <= len(avail_stock):
            item = avail_stock[pick-1]
            local_price = get_price(item, player)
            player['money'] = buying(player, local_price)
            # tambah isi warehouse
        else:
            print("Barang tidak ditemukan.")

    elif option == "jual":
        avail_stock = player["warehouse"] #for the warehouse implementation
        pick = int(input("Ketik [INDEX] barang yang ingin dijual.\n> "))
        # bikin bulk selling (bagian.split())
        # local_price = get_price(isi warehous, player)
        # player['money'] = selling(player, local_price)
        # kurangi isi warehouse
    return player['money']

# Intro game
print("\nKamu adalah Sakamoto Tatsuma, kapten dari Kaientai Space Trading Company.")
print("Suatu hari, wakil kapten Mutsu yang selalu mengerjakan pekerjaanmu"\
      "\ntiba-tiba merasa malas dan menyuruh kamu bekerja.")

while True:
    print(f"\nPlanet: {player['cur_planet']} | Uang: {player['money']} | Uang lokal: {mto_local(player['money'], player)}")
    pilihan = input("Ketik 'khelp' untuk melihat perintah.\n> ").split()
    if not pilihan:
        continue
    elif pilihan[0] == "khelp":
        print("\nPERINTAH")
        print("1. kt    -> travel" \
              "\n2. ks  -> shop di planet ini")
    elif pilihan[0] == "kt":
        travel(player)
    elif pilihan[0] == "ks": 
        hasil = openshop_andpick(player)
        if hasil != None:
            player['money'] = hasil
    else:
        print("Perintah tidak ditemukan!")