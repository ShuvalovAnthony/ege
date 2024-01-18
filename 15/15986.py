for a in range(300, 0, -1):
    flag = True

    for x in range(300):
        for y in range(300):
            if not (
                (y + 2*x != 48) or
                (a < x) or
                (x < y)
            ):
                flag = False


    if flag:
        print('Otvet = ', a)
        break