from itertools import *


def f(x, y, z, w):
    return (((x and y) <= ((not(z)) or w)) and (((not(w)) <= x) or (not(y))))


for a in product([0, 1], repeat=6):
    t = [(1, a[0], 1, 1), (0, a[1], a[2], 0), (1, a[3] , a[4], a[5])]
    
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))