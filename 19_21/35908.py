def f19(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 93) and (step == 3): return True
    elif (
        ((s1 + s2 >= 93) and (step < 3)) or # перебор раньше чем надо
        ((s1 + s2 < 93) and (step == 3)) # недобор когда надо
    ): return False

    return (
        f19(s1 + 1, s2, step + 1) or
        f19(s1*2, s2, step + 1) or
        f19(s1, s2 + 1, step + 1) or
        f19(s1, s2*2, step + 1)
    )

print("----- zadacha 19 ------")
for s2 in range(1, 80 + 1):
    if f19(12, s2):
        print(s2)
        break


def f20(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 93) and (step == 4): return True
    elif (
        ((s1 + s2 >= 93) and (step < 4)) or # перебор раньше чем надо
        ((s1 + s2 < 93) and (step == 4)) # недобор когда надо
    ): return False

    if step%2 == 1:
        return (
            f20(s1 + 1, s2, step + 1) or
            f20(s1*2, s2, step + 1) or
            f20(s1, s2 + 1, step + 1) or
            f20(s1, s2*2, step + 1)
        )
    
    return (
            f20(s1 + 1, s2, step + 1) and
            f20(s1*2, s2, step + 1) and
            f20(s1, s2 + 1, step + 1) and
            f20(s1, s2*2, step + 1)
        )

print("----- zadacha 20 ------")
for s2 in range(1, 80 + 1):
    if f20(12, s2):
        print(s2)


def f21(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 93) and (step == 3): return True
    elif (
        ((s1 + s2 >= 93) and (step < 3)) or # перебор раньше чем надо
        ((s1 + s2 < 93) and (step == 3)) # недобор когда надо
    ): return False

    if step%2 == 0:
        return (
            f21(s1 + 1, s2, step + 1) or
            f21(s1*2, s2, step + 1) or
            f21(s1, s2 + 1, step + 1) or
            f21(s1, s2*2, step + 1)
        )
    
    return (
            f21(s1 + 1, s2, step + 1) and
            f21(s1*2, s2, step + 1) and
            f21(s1, s2 + 1, step + 1) and
            f21(s1, s2*2, step + 1)
        )

print("----- zadacha 21 ------")
for s2 in range(1, 80 + 1):
    if f21(12, s2):
        print(s2)