# https://kompege.ru/variant?kim=25019383

from itertools import *

def f(x, y, z, w):
    return (not (w <= z)) or (x <= y) or (not x)


for a in product([0, 1], repeat=7): # repeat 7 - колво ПУСТЫХ ячеек
    # t - строки таблицы, 1 кортеж = 1 строка (БЕЗ F)
    # пустая ячейка -> a[i] где i не повторяется (по порядку идут)
    # repeat 7 -> 0...6 (всего 7 шт)
    t = [
        (1, a[0], a[1], a[2]),
        (0, 1, 0, a[3]),
        (a[4], 0, a[5], a[6])
        ]

    if len(t) == len(set(t)): # убираем повторяющиеся строки
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                for r in t:
                    print(''.join(p))