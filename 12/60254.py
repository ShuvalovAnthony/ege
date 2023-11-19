def algo(s):
    while ('52' in s) or ('2222' in s) or ('1122' in s):
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)

    return s


def summa_cifr(s: str):
    return sum([int(i) for i in s])


for i in range(1000, 3, -1):
    s = '5' + '2'*i

    if summa_cifr(
        algo(s)
    ) == 64:
        print(i)
        break