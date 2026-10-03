# def total(n):
#     if n == 1:
#         return 1
#     return n + total(n -1)

# n = int(input("Masukkan n: "))
# print(f"total penjumlahan 1 hingga {n} adalah {total(n)}")

# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# n = int(input("Masukkan n: "))
# print(f"Faktorial {n} adalah {factorial(n)}")

# def grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     else:
#         return "F"

# score_raw = input("Input score: ").strip()
# try:
#     score = int(score_raw)
#     if 0 <= score <= 100:
#         print(f"Your grade is {grade(score)}!")
#     else:
#         print("Score has to be a number from 0 to 100.")
# except ValueError:
#     print("Score has to be a number from 0 to 100.")