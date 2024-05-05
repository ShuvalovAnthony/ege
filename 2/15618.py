from itertools import *

def f(x, y, w, z):
    return (x and not y) or (y == z) or not w


for a in product([0, 1], repeat=5):
    t = [
        (a[0], 0, a[1], a[2]),
        (1, 0, a[3], 0),
        (1, a[4], 0, 0)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p)