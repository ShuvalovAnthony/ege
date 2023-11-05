for n in range(255, 0, -1):
    n_bin = bin(n)[2::].zfill(8)

    r = int(n_bin, 2)
    if 255 - 2*n == 133:
        print(r)