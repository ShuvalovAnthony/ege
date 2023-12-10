from itertools import combinations


def p(x):
    return 20 <= x <= 50


def q(x):
    return 30 <= x <= 65


def a(start, stop, x):
    return start <= x <= stop


coords = combinations(
    sorted([20, 50, 30, 65]), 
    2
)

dlini_otrezkov = set()


for start, stop in coords:
    flag = True

    for x in range(1, 100):
        if not (
            (not a(start, stop, x)) <=
            (
                p(x) <= (not q(x))
            )
        ):
            flag = False
            break

    if flag:
        dlini_otrezkov.add(stop - start)


print(dlini_otrezkov, min(dlini_otrezkov))

