for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not (
            (not (x%a == 0)) <=
            (
                (x%28 == 0) <=
                (not(
                    x%49 == 0
                ))
            )
        ):
            flag = False
            break

    if flag:
        print(a)