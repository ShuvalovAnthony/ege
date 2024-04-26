def sumNaibDvuh(num: int):
    deliteli = []
    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.append(i)
            deliteli.append(num//i)
    deliteli = sorted(deliteli, reverse=True)[1:]
    if len(deliteli) >= 2: return deliteli[0] + deliteli[1]
    return 0


limit = 5
for num in range(10**7, 10**19):
    res = sumNaibDvuh(num)
    if 0 < res < 10000:
        print(res)
        limit -= 1

    if not limit: break