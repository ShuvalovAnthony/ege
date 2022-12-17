for x in range(1, 100):
    for s in range(1, 10**5):
        s = 100*s + x
        n = 1
        while s < 2021:
            s += 5*n
            n += 1
        if n == 17:
            print(x)
            break