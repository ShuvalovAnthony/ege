def getExp(n):
    for i in range(1, 30):
        if 2**i >= n:
            return i
        


for n in range(1000, 0, -1):
    if (
        ((110 + getExp(n)) + 7)//8 + 50
        )*n <= 30*1024:
        print(n)
        break
