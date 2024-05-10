from string import digits, ascii_lowercase

num = 3*1024**75 + 2*256**76 - 16**77 - 2023

alph = digits + ascii_lowercase[:22]

digits = ''

while num > 0:
    digits += (alph[num%32])
    num //= 32

print(digits.count('0'))