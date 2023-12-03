def del_(n, m):
    return n%m == 0


for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        if not (
            (del_(x, 2) <= (not del_(x, 3))) or
            (x + a >= 100)
        ):
            flag = False
            break

    if flag:
        print(a)
        break
