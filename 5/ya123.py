# функция перевода в троичную систему счисления
# заменив 3 на любое число до 10 можем получить
# перевод и в другие системы

def toTri(num: int):
    res = ''
    while num > 0: # делим число, пока оно есть и записываем остатки в res
        res += str(num%3) # где 3 - система счисления
        num //= 3 # где 3 - система счисления
    return res[::-1] # переворачиваем строку


def summaCifr(num: str):
    return sum([int(i) for i in num])


res = []

for n in range(1000):
    tri = toTri(n)

    if summaCifr(tri)%2 == 0:
        tri = '2' + tri[2:] + '0'
    else:
        tri = '20' + tri[2:] + '1'

    r = int(tri, 3)


    if r > 75:
        res.append([r, n])

print(min(res, key=lambda x: x[0]))
