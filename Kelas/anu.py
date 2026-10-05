# def new_day():

# while ??? == True:
# 	new_day()

def kuiskalkulus():
    soalkuiskalkulus = [1,2,3,4,5]
    jawaban_kuiskalkulus_Narendra = []
    jawaban_kuiskalkulus_Raka_NIM = []
    jawaban_kuiskalkulus_Bobby_NIM = []

    for i, soal in enumerate(soalkuiskalkulus, start=1):
        jaw_naren = input(f"\nMasukkan jawaban Naren ke-{i}: ")
        jawaban_kuiskalkulus_Narendra.append(jaw_naren) 
    print("Naren selesai menjawab.")

    for i, soal in enumerate(soalkuiskalkulus, start=1):
        jaw_raka = input(f"\nMasukkan jawaban Raka ke-{i}: ")
        jawaban_kuiskalkulus_Raka_NIM.append(jaw_raka)
    print("Raka selesai menjawab.")

    for i, soal in enumerate(soalkuiskalkulus, start=1):
        jaw_anu = input(f"\nMasukkan jawaban anu ke-{i}: ")
        jawaban_kuiskalkulus_Bobby_NIM.append(jaw_anu)
    print("anu selesai menjawab.")

    for i, nomor_soal in enumerate(soalkuiskalkulus):
        if nomor_soal % 2 != 0:
            if jawaban_kuiskalkulus_Narendra[i] != jawaban_kuiskalkulus_Raka_NIM[i]:
                jawaban_kuiskalkulus_Narendra[i] = jawaban_kuiskalkulus_Raka_NIM[i]
        else:
            if jawaban_kuiskalkulus_Narendra[i] != jawaban_kuiskalkulus_Bobby_NIM[i]:
                jawaban_kuiskalkulus_Narendra[i] = jawaban_kuiskalkulus_Bobby_NIM[i]

    print(f"\nJawaban Naren: {jawaban_kuiskalkulus_Narendra}")
    print(f"Jawaban Raka: {jawaban_kuiskalkulus_Raka_NIM}")
    print(f"Jawaban anu: {jawaban_kuiskalkulus_Bobby_NIM}")

# def penambahansaldo():
#     saldo_gopay_081545553379 = 250000    
#     if tekanan_rongga_dada_Narendra > -4 or tekanan_rongga_dada_Narendra < -8: 
#         saldo_gopay_081545553379 += 1000

deadline_logma = (17,0,0) #jadi tuple.