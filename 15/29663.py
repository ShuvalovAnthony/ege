for a in range(10**4, 1, -1):
    flag = True
    for x in range(1, 1000):
        if not ((a < 50) and ((x%a != 0) <= ((x%10 == 0) <= (x%12 != 0)))):
            flag = False
    if flag:
        print('OTVET', a)
        break