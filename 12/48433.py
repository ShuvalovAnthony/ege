for n in range(1, 200):
    s = '0' + '1'*n + '2'*n +'0'

    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)

    if (s.count('1') == 40) and (s.count('2') > 50):
        print(s.count('2'))

