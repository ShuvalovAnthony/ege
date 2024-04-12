from itertools import *


def f1(x, y, z, w):
    return (w == x) and (y <= z)

def f2(x, y, z, w):
    return (w <= x) <= (y == z)


for a in product([0, 1], repeat=5): # 0, 1, 2, 3, 4
    t = [
        (1, a[0], 1, 1),
        (a[1], 1, 0, 0),
        (a[2], 0, 0, a[3])
    ]
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if (
                ([f1(**dict(zip(p, row))) for row in t] == [1, 1, 0]) and
                ([f2(**dict(zip(p, row))) for row in t] == [0, a[4], 0])
            ):
                print(*p)