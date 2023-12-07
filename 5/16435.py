for n in range(1, 10000):
    bin_n = bin(n)[2:-1]

    if n%2: # тоже самое, что и n%2 == 1
        bin_n += '10'
    else:
        bin_n += '01'

    r = int(bin_n, 2)

    if r == 2017:
        print(n)