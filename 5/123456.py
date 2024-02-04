def to5(num):
    res = ''
    while num > 0:
        res += str(num%5)
        num //= 5
    return res[::-1]



for n in range(1, 10**4):
    n_5 = to5(n)

    if n%25 == 0:
        n_5 = n_5[-3:] + n_5
    else:
        n_5 += to5(n%25)

    r = int(n_5, 5)

    if r > 10000:
        print(n)
        break