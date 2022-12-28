for s in range(10**6, 0, -1):
    start_s = s
    s //= 10
    n = 1
    while s < 51:
        s += 5
        n *= 2
    if n == 64:
        print(start_s)
        break
        
