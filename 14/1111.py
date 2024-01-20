num = abs(18*7**108 - 5*49**76 + 343**35 - 50)

summa_cifr = 0

while num > 0:
    summa_cifr += num%49
    num //= 49

print(summa_cifr)