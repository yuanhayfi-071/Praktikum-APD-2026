# Setting karakter
visa = 0 # Tiap cur_planet punya deadline visa yg berbeda.
money = 1000000
cur_planet = "O-Edo" # cur_planet starter

# Map
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
def travel():
    planetnames = list(planets)
    print("\nDESTINASI")
    for i, name in enumerate(planetnames, start=1):
        print(f"{i}. {name}")
    destination = int(input("Ketik [INDEKS] destinasi.\n> "))
    if cur_planet != planetnames[destination-1]:
        moveto_planet = planetnames[destination-1]
        print(f"Berangkat ke {moveto_planet}...")
        return moveto_planet
    else: 
        print(f"Sudah berada di {cur_planet}!")
        return cur_planet

def mto_local(amount, cur_planet): # Hitung base dalam local rate (kyknya bakal dipake buat uang lu doang)
    return amount / planets[cur_planet]["rate"]

def mto_base(amount, cur_planet): # Hitung local price dalam base 
    return amount * planets[cur_planet]["rate"]

def get_price(item, cur_planet): # Hitung local price
    return items[item]["base_price"] * planets[cur_planet]["mod_price"][item]

def buying(local_price, cur_planet):
    price_inbase = mto_base(local_price, cur_planet)
    if money >= price_inbase:
        money -= price_inbase
        print("\nBerhasil membeli!")
        print(f"Uang: {money}")

def selling(local_price, cur_planet):
    price_inbase = mto_base(local_price, cur_planet)
    money += price_inbase
    print("\nBerhasil menjual!")
    print(f"Uang: {money}")

def show_window(cur_planet):
    print(f"\nSTOK PLANET {cur_planet.upper()}")
    for i, item in enumerate(planets[cur_planet]["stock"], start=1):
        local_price = get_price(item, cur_planet)
        print(f"{i}. {item}, local cost: {local_price} / base cost: {mto_base(local_price, cur_planet)}")

    print(f"\nRATE HARGA PLANET {cur_planet.upper()}")
    for item in planets[cur_planet]['mod_price']:
        local_price = get_price(item, cur_planet)
        print(f"- {item}: {local_price} (x{planets[cur_planet]['mod_price'][item]})")

def openshop_andpick(cur_planet):
    show_window(cur_planet)

    option = input("\nKetik beli atau jual.\n> ")
    if option == "beli":
        pick = input("Ketik satu [INDEX] barang.\n> ")
        if 1 <= int(pick) <= len(planets[cur_planet]["stock"]):
            buying(get_price(items[pick],cur_planet),cur_planet)
        else:
            print("Barang tidak ditemukan.")

    elif option == "jual":
        pick = input("Ketik nama satu barang yang ingin dijual.\n> ")
        selling(get_price(pick, cur_planet), cur_planet)

# Intro game
print("\nKamu adalah Sakamoto Tatsuma, kapten dari Kaientai Space Trading Company.")
print("Suatu hari, wakil kapten Mutsu yang selalu mengerjakan pekerjaanmu"\
      "\ntiba-tiba merasa malas dan menyuruh kamu bekerja.")

while True:
    print(f"\nPlanet: {cur_planet} | Uang: {money} | Uang lokal: {mto_local(money, cur_planet)}")
    pilihan = input("Ketik 'khelp' untuk melihat perintah.\n> ")
    if pilihan == "khelp":
        print("\nPERINTAH")
        print("1. kt    -> travel" \
              "\n2. ks  -> shop di planet ini")
    elif pilihan == "kt":
        cur_planet = travel()
    elif pilihan == "ks":
        openshop_andpick(cur_planet)