for n in range(1, 10**6):
    start_n = n

    n = bin(n)[2::] # строим двоичную запись числа n, type - str

    for i in range(2):
        summa_cifr = 0
        for i in n:
            summa_cifr += int(i)
        n += str(summa_cifr%2)

    r = int(n, 2)
    if r > 77:
        print(start_n)
        break