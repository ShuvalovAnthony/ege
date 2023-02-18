from itertools import combinations

def d(x):
    return 17 <= x <= 58

def c(x):
    return 29 <= x <= 80

def a(start, stop, x):
    return start <= x <= stop

coords = combinations([17, 29, 58, 80], 2)

dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if not (d(x) <= (((not c(x)) and (not a(start, stop, x))) <= (not d(x)))):
            flag = False
            break

    if flag:
        dlini.append(stop - start)

print(dlini)