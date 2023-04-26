num = 3*64**1073 - 2*16**1131 + 4**1173 - 484

cifri = []

while num > 0:
    cifri.append(num%4)
    num //= 4

for i in range(4):
    print(i, cifri.count(i))

