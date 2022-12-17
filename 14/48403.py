for x in '0123456789AB':
    summa = int('2AB' + x, 12) + int(x + '8E', 17)
    if summa%27 == 0:
        print(summa//27)
        # break