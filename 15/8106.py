# ДЕЛ(n, m) <-> n%m == 0

for a in range(1, 1000): # a = 7
    flag = True
    for x in range(1, 1000):
        if not ((x%a != 0) <= ((x%6 == 0) <= (x%4 != 0))):
            flag = False
            break
    if flag:
        print('OTVET', a)
        