def toTri(num: int):
    res = ''
    while num > 0:
        res += str(num%3)
        num //= 3
    return res[::-1]


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
