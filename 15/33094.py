def del_(n, m):
    return n%m == 0


for a in range(10**5, 0, -1):
    flag = True

    for x in range(1, 10**5):
        if not (
            (a < 50) and
            (
                (not del_(x, a)) <=
                (
                    del_(x, 10) <=
                    (not del_(x, 18))
                )
            )
        ):
            flag = False
            break


    if flag:
        print(a)
        break