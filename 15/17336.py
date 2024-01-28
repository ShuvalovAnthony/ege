for a in range(0, 300):
    flag = True

    for x in range(0, 300):
        for y in range(0, 300):
            if not(
                (3*x + 4*y != 60) or 
                ((a >= x) and (a >= y))
            ):
                flag = False

    if flag:
        print(a)
        break