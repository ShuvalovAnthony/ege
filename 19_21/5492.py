def f19(s1, s2, step=1):  # p-1 v-2 -p3 v-4 p-5
    if ((s1 + s2) > 60) and (step == 3):
        return 1
    elif (
        ((s1 + s2) > 60) or
        ((s1 + s2) <= 60) and (step == 3)
    ):
        return 0
    # s1 - min s2 - max
    s1, s2 = min(s1, s2), max(s1, s2)
    if step % 2:
        return f19(s1 + 1, s2, step + 1) and\
            f19(s1 + 2, s2, step + 1) and\
            f19(s1*2, s2, step + 1)
    return f19(s1 + 1, s2, step + 1) or\
        f19(s1 + 2, s2, step + 1) or\
        f19(s1*2, s2, step + 1)


for s2 in range(1, 53):
    if f19(8, s2):
        print(s2)
        break

print('-'*10)


def f20(s1, s2, step=1):  # p-1 v-2 -p3 v-4 p-5
    if ((s1 + s2) > 60) and (step == 4):
        return 1
    elif (
        ((s1 + s2) > 60) or
        ((s1 + s2) <= 60) and (step == 4)
    ):
        return 0
    # s1 - min s2 - max
    s1, s2 = min(s1, s2), max(s1, s2)
    if step % 2 == 0:
        return f20(s1 + 1, s2, step + 1) and\
            f20(s1 + 2, s2, step + 1) and\
            f20(s1*2, s2, step + 1)

    return f20(s1 + 1, s2, step + 1) or\
        f20(s1 + 2, s2, step + 1) or\
        f20(s1*2, s2, step + 1)


stones = []
for s2 in range(1, 53):
    if f20(8, s2):
        stones.append(s2)
print(min(stones), max(stones))

print('-'*10)


def f21(s1, s2, step=1):  # p-1 v-2 -p3 v-4 p-5
    if ((s1 + s2) > 60) and (step in (3, 5)):
        return 1
    elif (
        ((s1 + s2) > 60) or
        ((s1 + s2) <= 60) and (step == 5)
    ):
        return 0
    # s1 - min s2 - max
    s1, s2 = min(s1, s2), max(s1, s2)
    if step % 2:
        return f21(s1 + 1, s2, step + 1) and\
            f21(s1 + 2, s2, step + 1) and\
            f21(s1*2, s2, step + 1)

    return f21(s1 + 1, s2, step + 1) or\
        f21(s1 + 2, s2, step + 1) or\
        f21(s1*2, s2, step + 1)


# ОТВЕТ НЕ СОШЕЛСЯ!!! проверить
for s2 in range(1, 53):
    if f21(8, s2):
        print(s2)
