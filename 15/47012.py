from itertools import combinations


def p(x):
    return 69 <= x <= 91


def q(x):
    return 77 <= x <= 114


def a(start, stop, x):
    return start <= x <= stop


coords = combinations(
    sorted([69, 91, 77, 114]), 2
)

dlini = set()
# ¬P ∨ ¬(P ≡ Q) ∨ ¬Q ∨ A


for start, stop in coords:
    flag = True
    for x in range(-150, 150):
        if not ((not p(x)) or (p(x) != q(x)) or (not q(x)) or a(start, stop, x)):
            flag = False
            break
    
    if flag:
        dlini.add(stop - start)

print(dlini, min(dlini))


