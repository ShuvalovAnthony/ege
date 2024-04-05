import sys

sys.set_int_max_str_digits(10000)

num = 4*3125**2019 + 3*625**2020 - \
    2*125**2021 + 25**2022 - 4*5**2023 - 2024


digits = []

while num > 0:
    digits.append(num%25)
    num //= 25


summa = 0
for i in range(11, 30):
    summa += digits.count(i)


print(summa)



