from itertools import *


def f(x, y, z, w):
    return ((1 == w) == (not ((w and x) or y))) <= z


for a in product([0, 1], repeat=10):
    t = [
        (a[0], a[1], 1, a[2]),
        (1, a[3], 1, a[4]),
        (0, 1, 0, 0),
        (1, a[5], 1, a[6]),
        (a[7], a[8], 1, a[9])
    ]
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1, 1]:
                print(''.join(p))