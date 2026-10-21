# you can actually print the error message with "except ValueError as e", 
# then print(e) or even print(type(e)) and print(repr(e))

# 1.1 paleolitikum
# while True:
#     password = input("\nMasukkan password.\n> ")
#     adaangka = False
#     if password[0].istitle():
#         for i in password:
#             if i.isdigit():
#                 adaangka = True
#         if adaangka == False:
#             print("Password harus mengandung angka.")
#             continue
#         if len(password) < 10:
#             print("Password minimal 10 karakter.")
#             continue
#     else:
#         print("Awalan password wajib kapital.")
#         continue
#     print("Password diterima!")

# 1.2 mezolitikum
# while True:
#     try:
#         password = input("\nMasukkan password.\n> ")
#         if len(password) < 10:
#             raise ValueError('Password minimal 10 karakter')
#         if password[0].istitle() == False:
#             raise ValueError('Huruf pertama password harus kapital.')
#         if any(char.isdigit() for char in password) == False:
#             raise ValueError('Password harus mengandung angka.')
#     except ValueError as e:
#         print(e)
#     else:
#         print("Password diterima!")

#2. input usia. usia < 0, error; usia < 17, error 'film khusus dewasa';
# valid, cetak. else cetak, finally tutup.

# while True:
#     try:
#         usia = input("Masukkan usia.\n> ")
#         if int(usia) < 0:
#             raise ValueError('Usia tidak boleh < 0.')
#         if usia.isdigit() and int(usia) < 17:
#             raise ValueError('Film khusus dewasa.')
#     except ValueError as e:
#         print(e)
#     else:
#         print("Mencetak tiket.")
#     finally:
#         print("Menutup program...")
#         exit()
            