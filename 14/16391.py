# num = 49**7 + 7**20 - 28
num = 1111

digits = []

while num > 0:
    digits.append(num%7)
    num //= 7

print(digits[::-1])