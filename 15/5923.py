from itertools import combinations

def p(x):
    return 5 <= x <= 280

def q(x):
    return 295 <= x <= 400

def r(x):
    return 375 <= x <= 450

def a(start, stop, x):
    return start <= x <= stop

coords = combinations([5, 280, 295,375, 400, 450], 2)

dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 1000):
        if not ((q(x) <= p(x)) or ((not a(start, stop, x)) <= r(x))):
            flag = False
            break

    if flag:
        dlini.append(stop - start)

print(dlini, min(dlini))