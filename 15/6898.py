from itertools import combinations

def f(n, m):
    return n%m == 0


def p(x):
    return 257 <= x <= 356

def q(x):
    return 5 <= x <= 600

def r(x):
    return 59 <= x <= 228

def a(start, stop, x):
    return start <= x <= stop


coords = combinations(
    sorted([257, 356, 5, 600, 59, 228]), 2
)


dlini = set()

for start, stop in coords:
    flag = True

    for x in range(0, 700):
        if not (
            (r(x) <= a(start, stop, x)) or
            ((f(x, 3) <= p(x)) <= (q(x) <= a(start, stop, x)))
        ):
            flag = False
            break

    if flag:
        dlini.add(stop - start)



print(dlini, min(dlini))