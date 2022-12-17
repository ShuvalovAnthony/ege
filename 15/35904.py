for a in range(1, 1000):
    flag = True

    for x in range(1, 1000):
        if not ((a%40 == 0) and ((780%x == 0) <= ((a%x != 0) <= (180%x != 0)))):
            flag = False
            break

    if flag:
        print(a)
        break







