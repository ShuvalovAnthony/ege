for n in range(1, 10**6):
    n = bin(n)[2::]

    summa_cifr = 0
    for i in n:
        summa_cifr += int(i)

    if summa_cifr%2 == 0:
        n += '00'
    else:
        n += '11'

    r = int(n, 2)
    if r > 114:
        print(r)
        break


