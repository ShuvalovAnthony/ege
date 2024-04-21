from itertools import product


def f19(h1, h2, step=1): # 1p 2v 3p
    if (h1 + h2 >= 40) and (step == 2): return True
    elif (step == 2): return False

    h1, h2 = max(h1, h2), min(h1, h2)

    return any([
        f19(h1, h2 + i, step + 1) for i in range(1, h2 + 1)
    ])


res = []

for h1, h2 in product(range(40), range(40)):
    if f19(h1, h2):
        res.append(h1 + h2)

print(min(res))