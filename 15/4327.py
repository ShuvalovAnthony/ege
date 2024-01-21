from itertools import combinations


def p(x): return 5 <= x <= 40

def q(x): return 41 <= x <= 54

def r(x): return 6 <= x <= 53

def a(x, start, stop): return start <= x <= stop


coords = combinations(
    sorted([5, 40, 41, 54, 6, 53]),
    2
)

dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if (
            (
                (not p(x)) <=
                q(x)
            ) and
            r(x) and
            (not a(x, start, stop))
            ):
            flag = False
            break

    if flag:
        dlini.append(stop - start)

print(dlini)
print(min(dlini))