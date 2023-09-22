from itertools import combinations

def p(x):
    return 5 <= x <= 30

def q(x):
    return 14 <= x <= 23

def a(start, stop, x):
    return start < x < stop


coords = combinations(
    sorted([5, 30, 14, 23]), 2)

dlini = set()

for start, stop in coords:
    flag = True
    for x in range(0, 100):
        if not (((p(x)) == (q(x))) <= (not (a(start, stop, x)))):
            flag = False
            break

    if flag:
        dlini.add(stop - start)


print(dlini, max(dlini))


