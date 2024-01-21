from itertools import combinations


def p(x):
    return 24 <= x <= 77


def q(x):
    return 47 <= x <= 92


def r(x):
    return 82 <= x <= 116


def a(x, start, stop):
    return start <= x <= stop


coords = combinations(
    sorted([24, 77, 47, 92, 82, 116]), 2
)


dlini = []

for start, stop in coords:
    flag = True

    for x in range(0, 150):
        if not (
            (
                not (
                    q(x) <=
                    (
                        p(x) or r(x)
                    )
                )
            ) <=
            (
                (not a(x, start, stop)) <=
                (not q(x))
            )
        ):
            flag = False


    if flag:
        dlini.append(stop - start)


print(dlini)
print(min(dlini))