for n in range(2, 1000):
    bin_n = bin(n)[2:]

    bin_n = bin_n[:-1] + bin_n[1]*2

    r = int(bin_n, 2)
    if r > 76:
        print(n)
        break
    