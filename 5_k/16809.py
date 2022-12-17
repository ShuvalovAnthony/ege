for n in range(255, 0, -1):
    n_bin = bin(n)[2::]
    n_bin = '0'*(8 - len(n_bin)) + n_bin
    r = int(n_bin, 2)
    if 255 - 2*n == 133:
        print(r)