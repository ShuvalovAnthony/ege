# ПРОВЕРИТЬ!!!

def f19(s1, s2, step=1 ):
    if (s1 == s2) and (step == 3): return 1
    elif (
        ((s1 == s2) and (step < 3)) or
        ((s1 != s2) and (step == 3))
    ): return 0

    s1, s2 = min(s1, s2), max(s1, s2)

    if step%2 == 1:
        return f19(s1 + 1, s2, step + 1) and\
            f19(s1 + 3, s2, step + 1)

    return f19(s1 + 1, s2, step + 1) or\
        f19(s1 + 3, s2, step + 1)

for s1 in range(1, 24):
    if f19(s1, 13):
        print(s1)

print('___')

def f20(s1, s2, step=1 ):
    if (s1 == s2) and (step == 4): return 1
    elif (
        ((s1 == s2) and (step < 4)) or
        ((s1 != s2) and (step == 4))
    ): return 0

    s1, s2 = min(s1, s2), max(s1, s2)

    if step%2 == 0:
        return f20(s1 + 1, s2, step + 1) and\
            f20(s1 + 3, s2, step + 1)

    return f20(s1 + 1, s2, step + 1) or\
        f20(s1 + 3, s2, step + 1)

for s1 in range(1, 24):
    if f20(s1, 13):
        print(s1)

print('__')

def f21(s1, s2, step=1):
    if (s1 == s2) and (step in (3, 5)):
        return 1
    elif (
        ((s1 == s2) and (step not in (3, 5))) or
        ((s1 != s2) and (step == 5))
    ): return 0

    s1, s2 = min(s1, s2), max(s1, s2)

    if step%2 == 1:
        return f21(s1 + 1, s2, step + 1) and\
            f21(s1 + 3, s2, step + 1)

    return f21(s1 + 1, s2, step + 1) or\
        f21(s1 + 3, s2, step + 1)

for s1 in range(1, 24):
    if f21(s1, 13):
        print(s1)