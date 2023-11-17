from itertools import combinations

def b(x):
    return 23 <= x <= 37

def c(x):
    return 41 <= x <= 73

def a(start, stop, x):
    return start <= x <= stop

coords = combinations(sorted([23, 37, 41, 73]), 2)

dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 1000):
        if (
            not (
                (
                    (not b(x)) <= c(x)
                ) <=
                a(start, stop, x)
            )
        ):
            flag = False
            break

    if flag:
        dlini.append(stop - start)

print(dlini, min(dlini))