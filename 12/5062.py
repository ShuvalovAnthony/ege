def algo(stroka: str):
    while '00' not in stroka:
        stroka = stroka.replace('011', '20', 1)
        stroka = stroka.replace('022', '10', 1)
        stroka = stroka.replace('01', '220', 1) # опечатка!! поменять
        stroka = stroka.replace('02', '110', 1) # местами эти строки
    return stroka


for i in range(1, 100):
    for j in range(1, 100):
        s = '0' + '1221'*i + '12'*j + '0'

        s = algo(s)

        if (s.count('1') == 47 and s.count('2') < 70):
            print(s.count('2'), i, j)
                


