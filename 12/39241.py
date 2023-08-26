def algo(stroka: str):
    while ('111' in stroka) or ('222' in stroka):
        stroka = stroka.replace('111', '22', 1)
        stroka = stroka.replace('222', '1', 1)
    return stroka


for i in range(201, 500):
    if '1' not in algo('1'*i):
        print(i)
        break