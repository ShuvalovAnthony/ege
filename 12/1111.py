for n in range(10_000, 2, -25):
    s = '5' + '2'*n
    while (
        '52' in s or
        '2222' in s or
        '1112' in s
    ):
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)

    summa_cifr = sum([int(i) for i in s])


    if summa_cifr == 1685:
        print('otvet', n)
        break