def del_(n, m):
    return n%m == 0


for a in range(1, 999):
    flag = True
    
    for x in range(1, 999):
        if not (
            (del_(x, 2) <= (not del_(x, 13))) or (x + a >= 1000)
        ):
            flag = False
            break

    if flag:
        print(a)
        break