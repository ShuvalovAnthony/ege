from itertools import combinations


def p(x):
    return 12 <= x <= 62


def q(x):
    return 32 <= x <= 92


# <= - наименьшая длина
# < - наибольшая
def a(x, start, stop):
    return start <= x <= stop


coords = combinations(
    sorted([12, 62, 32, 92]),
    2
)

# список, в котором я храню длины подошедших отрезков А
dlini = []


for start, stop in coords:
    flag = True

    for x in range(0, 100):
        if not (
            (
                (not a(x, start, stop)) and
                q(x)
            ) <=
            (
                p(x)
            )
        ):
            flag = False
            break

    if flag:
        dlini.append(stop - start)



print(dlini)
print(min(dlini))
