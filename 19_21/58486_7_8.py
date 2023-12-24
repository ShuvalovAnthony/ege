from itertools import product


def f19(h1, h2, step=1):
    if ((h1 >= 48) or (h2 >= 48)) and (step == 2): return True
    elif (
        ((h1 < 48) and (h2 < 48)) and (step == 2)
    ): return False

    if h1 < h2: h1, h2 = h2, h1

    if h1 == h2:
        return (
        any(f19(h1 + i, h2, step + 1) for i in (1, 2, 3)) or
        any(f19(h1, h2 + i, step + 1) for i in (1, 2, 3))
        )

    return (
        any(f19(h1 + i, h2, step + 1) for i in (1, 2, 3)) or
        f19(h1, h2*2, step + 1)
    )


for h1, h2 in product(range(1, 48), range(1,48)):
    if f19(h1, h2):
        print(h1 + h2)
        print('-'*20)
        break


def f20(h1, h2, step=1):
    if ((h1 >= 48) or (h2 >= 48)) and (step == 4): return True
    elif (
        ((h1 < 48) and (h2 < 48)) and (step == 4) or
        ((h1 >= 48) or (h2 >= 48)) and (step < 4)
    ): return False

    if h1 < h2: h1, h2 = h2, h1

    if step%2 == 0:
        if h1 == h2:
            return (
            all(f20(h1 + i, h2, step + 1) for i in (1, 2, 3)) and
            all(f20(h1, h2 + i, step + 1) for i in (1, 2, 3))
            )

        return (
            all(f20(h1 + i, h2, step + 1) for i in (1, 2, 3)) and
            f20(h1, h2*2, step + 1)
        )

    if h1 == h2:
        return (
        any(f20(h1 + i, h2, step + 1) for i in (1, 2, 3)) or
        any(f20(h1, h2 + i, step + 1) for i in (1, 2, 3))
        )

    return (
        any(f20(h1 + i, h2, step + 1) for i in (1, 2, 3)) or
        f20(h1, h2*2, step + 1)
    )

answ = []
for h2 in range(1, 48):
    if f20(13, h2):
        answ.append(h2)

print(min(answ), max(answ))
print('-'*20)




def f21(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if ((h1 >= 48) or (h2 >= 48)) and (step in (3, 5)): return True
    elif (
        ((h1 < 48) and (h2 < 48)) and (step == 5) or
        ((h1 >= 48) or (h2 >= 48)) and (step < 5)
    ): return False

    if h1 < h2: h1, h2 = h2, h1

    if step%2:
        if h1 == h2:
            return (
            all(f21(h1 + i, h2, step + 1) for i in (1, 2, 3)) and
            all(f21(h1, h2 + i, step + 1) for i in (1, 2, 3))
            )

        return (
            all(f21(h1 + i, h2, step + 1) for i in (1, 2, 3)) and
            f21(h1, h2*2, step + 1)
        )


    if h1 == h2:
        return (
        any(f21(h1 + i, h2, step + 1) for i in (1, 2, 3)) or
        any(f21(h1, h2 + i, step + 1) for i in (1, 2, 3))
        )

    return (
        any(f21(h1 + i, h2, step + 1) for i in (1, 2, 3)) or
        f21(h1, h2*2, step + 1)
    )


for h2 in range(1, 48):
    if f21(39, h2):
        print(h2)
        break
