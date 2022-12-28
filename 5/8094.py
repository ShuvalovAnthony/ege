for n in range(1, 10**6):

    n_bin = bin(n)[2::] # строим двоичную запись числа n, type - str

    for i in range(2):
        summa_cifr = n_bin.count('1')
        n_bin += str(summa_cifr%2)

    r = int(n_bin, 2)
    if r > 43:
        print(r)
        break
        
        