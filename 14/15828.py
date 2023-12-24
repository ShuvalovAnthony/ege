num = 36**8 + 6**20 - 12

cifri = []

while num > 0:
    cifri.append(num%6)
    num //= 6

print(cifri.count(5))