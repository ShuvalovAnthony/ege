def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 107) and (step == 3): return True
    elif (
        ((h1 + h2 >= 107) and (step < 3)) or
        ((h1 + h2 < 107) and (step == 3))
    ): return False

    return any([
        f19(h1 + 1, h2, step + 1),
        f19(h1, h2 + 1, step + 1),
        f19(h1*2, h2, step + 1),
        f19(h1, h2*2, step + 1),
    ])


print('-------19------')
for h2 in range(1, 94):
    if f19(13, h2):
        print(h2)
        break



def f20(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 107) and (step == 4): return True
    elif (
        ((h1 + h2 >= 107) and (step < 4)) or
        ((h1 + h2 < 107) and (step == 4))
    ): return False

    if step%2 == 0:
        return all([
        f20(h1 + 1, h2, step + 1),
        f20(h1, h2 + 1, step + 1),
        f20(h1*2, h2, step + 1),
        f20(h1, h2*2, step + 1),
    ])

    return any([
        f20(h1 + 1, h2, step + 1),
        f20(h1, h2 + 1, step + 1),
        f20(h1*2, h2, step + 1),
        f20(h1, h2*2, step + 1),
    ])


print('-------20------')
for h2 in range(1, 94):
    if f20(13, h2):
        print(h2)
        


def f21(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 107) and (step in (3, 5)): return True
    elif (
        ((h1 + h2 >= 107) and (step < 5)) or
        ((h1 + h2 < 107) and (step == 5))
    ): return False

    if step%2:
        return all([
        f21(h1 + 1, h2, step + 1),
        f21(h1, h2 + 1, step + 1),
        f21(h1*2, h2, step + 1),
        f21(h1, h2*2, step + 1),
    ])

    return any([
        f21(h1 + 1, h2, step + 1),
        f21(h1, h2 + 1, step + 1),
        f21(h1*2, h2, step + 1),
        f21(h1, h2*2, step + 1),
    ])


print('-------20------')
for h2 in range(1, 94):
    if f21(13, h2):
        print(h2)
        break