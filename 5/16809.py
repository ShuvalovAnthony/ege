for n in range(255, 0, -1):
    n_bin = bin(n)[2::].zfill(8)

    r = int(n_bin, 2)
    if 255 - 2*n == 133:
        print(r)



for n in range(0, 256):
    # _ _ _ _ _ _ _ _

    bin_n = bin(n)[2:] # bin(n)[2:].zfill(8)
    bin_n = '0'*(8 - len(bin_n)) + bin_n

    bin_n = bin_n.replace('1', '2')
    bin_n = bin_n.replace('0', '1')
    bin_n = bin_n.replace('2', '0')

    r = int(bin_n, 2) - n

    if r == 133:
        print(n)
        break