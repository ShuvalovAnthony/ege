for n in range(1, 10**9): # десятичная
    bin_n = bin(n)[2:] # двоичная

    for i in range(3):
        summa_cifr = sum(list(map(int, list(str(int(bin_n, 2))))))
        if summa_cifr%2:
            bin_n += '1'
        else:
            bin_n += '0'
    r = int(bin_n, 2)

    if r > 1028:
        print(r, n)
        break
    
# 1035 RRRRRRR