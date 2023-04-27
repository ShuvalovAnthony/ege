from itertools import combinations

def p(x):
    return 257 <= x <= 1000

def q(x):
    return 5 <= x <= 100

def r(x):
    return 99 <= x <= 258

def a(start, stop, x):
    return start <= x <= stop

# УМНОЖАЕМ СПИСОК НА 2 чтобы проверить 0ые длины
coords = combinations(sorted([257, 1000, 5, 100, 99, 258]*2), 2)

dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 5000):
        if not (
            ((not a(start, stop, x)) or r(x)) and
            ((not a(start, stop, x)) or p(x) or q(x))
        ):
            flag = False
            break

    if flag:
        dlini.append(stop - start)

print(dlini, min(dlini))