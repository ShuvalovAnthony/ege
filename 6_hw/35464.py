for s in range(10**6):
    start_s = s
    s = 10*s + 5
    n = 1
    while s < 2021:
        s = s + 2*n
        n += 1
    if n == 11:
        print(start_s)