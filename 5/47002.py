for n in range(1, 10**5):
    n_bin = bin(n)[2:]

    r = n_bin[1::2].count('1') - n_bin[::2].count('0')

    if r == 4:
        print(n)
        break