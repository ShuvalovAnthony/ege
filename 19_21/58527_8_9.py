from itertools import product


def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if ((h1 >= 40) or (h2 >= 40)) and (step == 2): return True
    elif (step == 2): return False

    h1, h2 = max(h1, h2), min(h1, h2)

    if h1 == h2:
        return any(
            [f19(h1 + i, h2, step + 1) for i in (1, 2, 3)]
        )

    return any(
        [f19(h1 + i, h2, step + 1) for i in (1, 2, 3)] +
        [f19(h1, h2*2, step + 1)]
    )


print('------19-----')
for h1, h2 in product(range(1, 40), range(1, 40)):
    if f19(h1, h2):
        print(h1 + h2)
        break



def f20(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if ((h1 >= 40) or (h2 >= 40)) and (step == 4): return True
    elif (
        (step == 4) or (h1 >= 40) or (h2 >= 40)
    ): return False

    h1, h2 = max(h1, h2), min(h1, h2)
    # ветка вани
    if step%2 == 0:
        if h1 == h2:
            return all(
                [f20(h1 + i, h2, step + 1) for i in (1, 2, 3)]
            )

        return all(
            [f20(h1 + i, h2, step + 1) for i in (1, 2, 3)] +
            [f20(h1, h2*2, step + 1)]
        )

    # ветка пети
    if h1 == h2:
        return any(
            [f20(h1 + i, h2, step + 1) for i in (1, 2, 3)]
        )

    return any(
        [f20(h1 + i, h2, step + 1) for i in (1, 2, 3)] +
        [f20(h1, h2*2, step + 1)]
    )


print('------20-----')
answ = []

for h2 in range(1, 40):
    if f20(11, h2):
        answ.append(h2)

print(min(answ), max(answ))




def f21(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if ((h1 >= 40) or (h2 >= 40)) and (step in (3, 5)): return True
    elif (
        (step == 5) or (h1 >= 40) or (h2 >= 40)
    ): return False

    h1, h2 = max(h1, h2), min(h1, h2)
    # ветка вани
    if step%2:
        if h1 == h2:
            return all(
                [f21(h1 + i, h2, step + 1) for i in (1, 2, 3)]
            )

        return all(
            [f21(h1 + i, h2, step + 1) for i in (1, 2, 3)] +
            [f21(h1, h2*2, step + 1)]
        )

    # ветка пети
    if h1 == h2:
        return any(
            [f21(h1 + i, h2, step + 1) for i in (1, 2, 3)]
        )

    return any(
        [f21(h1 + i, h2, step + 1) for i in (1, 2, 3)] +
        [f21(h1, h2*2, step + 1)]
    )


print('------21-----')

for h2 in range(1, 40):
    if f21(31, h2):
        print(h2)
        break
