from itertools import combinations

def p(x):
    return 10 <= x <= 40

def q(x):
    return 5 <= x <= 15

def r(x):
    return 35 <= x <= 50

def a(start, stop, x):
    return start <= x <= stop # <= - если наименьшая, < - если наибольшая

# пишу все координаты из всех отрезков
coords = combinations(
    sorted([10, 15, 20, 5]), 2)

dlini = set()

for start, stop in coords:
    flag = True
    for x in range(0, 60): # проверяем диапазон х
        if not ( 
            # пишем логическое выражение
            (a(start, stop, x) or p(x)) or
            (q(x) <= r(x))
        ):
            flag = False
            break

    if flag: # добавляем в множество длину отрезка - START - STOP !!!
        dlini.add(stop - start)


print(dlini, min(dlini))


