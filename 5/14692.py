for n in range(9999, 999, -1):
    n = str(n)

    summ_12 = int(n[0]) + int(n[1])
    summ_23 = int(n[1]) + int(n[2])
    summ_34 = int(n[2]) + int(n[3])

    summs = sorted([summ_12, summ_23, summ_34])[1:]

    res = str(summs[0]) + str(summs[1])

    if res == '613':
        print(n)
        break