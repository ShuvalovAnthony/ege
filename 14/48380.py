for a in range(1, 1000):
    for x in '0123456789AB':
        m = int('49' + x + '26', 12)
        n = int('49' + x + '70', 12)
        if (m + a)%n == 0:
            print(a)