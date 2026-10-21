import random

RATES = {5: 0.051, 4: 0.006}

def build_rarity(banner_name): #creating the chosen banner's pool
    pool = {} #honestly this step is only for the sake of doing droprates based on rarity
    for item_id in banners[banner_name]['pool']:
        rarity = masterlist[item_id]['rarity']
        pool.setdefault(rarity, []).append(item_id) #"look inside the pool and if you find key rarity alr, just append. else, create the dict of rarity then append."
        #now your pool look like {5: {id1,id2}, 4: {id3,id4}}
    return pool

def pull(banner_name):
    pool = build_rarity(banner_name)
    rarity = random.choices(list(RATES), weights=RATES.values())[0] #pulling the rarity affected by rates, RATES is turned into list
    item_id = random.choice(pool[rarity]) #pulling the char from recieved rarity
    return masterlist[item_id]

masterlist = {
    "m001": {"name":"diluc","element":"pyro","rarity":5},
    "m002": {"name":"jean","element":"anemo","rarity":5},
    "m003": {"name":"mona","element":"hydro","rarity":5},

    "d001": {"name":"alhaitham","element":"dendro","rarity":5},
    "d002": {"name":"nahida","element":"dendro","rarity":5},
    "d003": {"name":"kaveh","element":"dendro","rarity":4},
    "d004": {"name":"tighnari","element":"dendro","rarity":5},
    "d005": {"name":"cyno","element":"electro","rarity":5},
    "d006": {"name":"sethos","element":"electro","rarity":4},
    "d007": {"name":"wanderer","element":"anemo","rarity":5},

    "z001": {"name":"zandik","element":"dendro","rarity":5},
    "z002": {"name":"il dottore: prime","element":"dendro","rarity":5},
    "z003": {"name":"il dottore: omega","element":"cryo","rarity":5},
    "z004": {"name":"il dottore: lambda","element":"pyro","rarity":5},
    "z005": {"name":"il dottore: delta","element":"geo","rarity":4},
    "z006": {"name":"il dottore: iota","element":"anemo","rarity":4},
    "z006": {"name":"il dottore: gamma","element":"hydro","rarity":4},
    "z007": {"name":"il dottore: omicron","element":"electro","rarity":4}
}

banners = {
    "standard": {
        "pool"      : ["m001","m002","m003","d004","d003","d006"],
        "featured"  : []
    },
    "dottore special": {
        "pool"      : ["z001","z002","z003","z004","z005","z006","z007"],
        "featured"  : ["z001","z002"]
    }
}

for banner in banners:
    print(f"- {banner}")

banner_name = input("\nMasukkan nama banner untuk dipull.\n> ")
hasil = pull(banner_name)
print(f"Mendapatkan {hasil['name']} | {hasil['element']} | {hasil['rarity']}* !")