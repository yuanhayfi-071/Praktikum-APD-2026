kuiskalkulus = [1,2,3]
kunciJawaban_kuisKalkulus_Cipto = ["12", "8", "Tidak ada", "54", "-∞", "∞"]
jawabanNarendra_NIM = []

for i, nomorsoal in enumerate(kuiskalkulus, start=1):
    simpan = input(f"Masukkan jawaban Narendra ke-{i}: ")
    jawabanNarendra_NIM.append(simpan)

for i in range(len(jawabanNarendra_NIM)):
    jawabanNarendra_NIM[i] = kunciJawaban_kuisKalkulus_Cipto[i]

print("")
for i, jawaban in enumerate(jawabanNarendra_NIM, start=1):
    print(f"Jawaban Narendra ke-{i}: {jawaban}")

deadline_logma = 17
deadline_logma = 12
print(deadline_logma)

deadline_logma = (17,0,0) #jadi tuple.
deadline_logma[0] = 12 #code error
print(deadline_logma)
    
Saldo_Narendra_NIM = 12000
CMUjungPulpen_Narendra_NIM = 0
SebelumnyaTertutup = True

while True:
    pencet = input("Ketik 'ya' untuk memencet pulpen.\n> ")
    if pencet.strip().lower() == "ya" and SebelumnyaTertutup:
        CMUjungPulpen_Narendra_NIM += 1
    elif pencet.strip().lower() == "ya" and not SebelumnyaTertutup:
        CMUjungPulpen_Narendra_NIM = 0

    if CMUjungPulpen_Narendra_NIM > 0 and SebelumnyaTertutup:
        Saldo_Narendra_NIM += 5000
        print("\nRp.5.000 barus saja ditransfer ke saldo Anda.")
    SebelumnyaTertutup = (CMUjungPulpen_Narendra_NIM == 0)