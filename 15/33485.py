for a in range(1000, 0, -1):
    flag = True
    for x in range(1, 1000):
        if not (
            (120 % a == 0) and
            (
                (x % a != 0) <=
                (
                    (x % 18 == 0) <=
                    (x % 24 != 0)
                )
            )
        ):
            flag = False
 
    if flag:
        print(a)
        break