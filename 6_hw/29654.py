for s in range(10**6):
    start_s = s
    n = 4
    while s < 37:
        s += 3
        n *= 2
    if n == 128:
        print(start_s)
        break

    