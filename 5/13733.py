for n in range(1, 10**3):
    n_bin = bin(n)[2:]
    n_bin += str(n_bin.count('1')%2)
    n_bin += str(n_bin.count('1')%2)

    r = int(n_bin, 2)

    if r > 83:
        print(r)
        break
