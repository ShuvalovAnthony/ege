num = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338

cifri = []

while num > 0:
    cifri.append(num%15)
    num //= 15

print(len(set(cifri)))