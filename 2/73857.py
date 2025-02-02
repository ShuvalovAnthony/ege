from itertools import product, permutations


def f(x, y, z, w):
    return (z == (x <= w)) and (x == (not (w <= y)))



for a in product([0, 1], repeat=4):
    t = [
        (0, a[0], 0, 0),
        (a[1], a[2], 0, 0),
        (1, 1, a[3], 0)
    ]

    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
                print(*p)