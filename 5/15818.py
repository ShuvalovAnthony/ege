for n in range(1, 1000):
    n_bin = bin(n)[2::] # '101010' str

    for i in range(2):
        summa_cifr = 0

        for cifra in n_bin:
            summa_cifr += int(cifra)

        n_bin += str(summa_cifr%2)


    # остаток от суммы цифр для ДВОИЧНОГО ЧИСЛА способ 2
    # for i in range(2):
    #     n_bin += str(n_bin.count('1')%2)

    r = int(n_bin, 2)
    if r > 93:
        print(r)
        break
        

