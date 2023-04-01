# https://kompege.ru/variant?kim=25019383
# xzyw
from itertools import *

def f1(x, y, z, w):
    return (x <= y) == (w or (not z))

def f2(x, y, z, w):
    return (x <= y) and ((not w) == z)



for a in product([0, 1], repeat=5): # repeat 7 - колво ПУСТЫХ ячеек
    # t - строки таблицы, 1 кортеж = 1 строка (БЕЗ F)
    # пустая ячейка -> a[i] где i не повторяется (по порядку идут)
    # repeat 7 -> 0...6 (всего 7 шт)
    t = [
        (a[0], 1, 0, 1),
        (a[2], 0, 0, 0),
        (0, a[4], 0, 0)
        ]

    if len(t) == len(set(t)): # убираем повторяющиеся строки
        for p in permutations('xywz'):
            if ([f1(**dict(zip(p, r))) for r in t] == [a[1], 0, 0] and
                [f2(**dict(zip(p, r))) for r in t] == [0, a[3], 1]
            ):
                for r in t:
                    print(''.join(p))