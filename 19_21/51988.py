def f19(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 > 80) and (step == 3): return True
    elif (
        ((s1 + s2 <= 80) and (step == 3)) or
        (s1 + s2 > 80)
    ): return False


    # s1 - min, s2 - max VSEGDA
    s1, s2 = min(s1, s2), max(s1, s2)

    if step%2 == 1:
        return (
            f19(s1 + 1, s2, step + 1) and
            f19(s1 + 2, s2, step + 1) and
            f19(s1*2, s2, step + 1)
        )
    
    return (
            f19(s1 + 1, s2, step + 1) or
            f19(s1 + 2, s2, step + 1) or
            f19(s1*2, s2, step + 1)
        )


print("Zadacha 19")
for s2 in range(1, 68 + 1):
    if f19(12, s2):
        print(s2)
        break



def f20(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 > 80) and (step == 4): return True
    elif (
        ((s1 + s2 <= 80) and (step == 4)) or
        (s1 + s2 > 80)
    ): return False


    # s1 - min, s2 - max VSEGDA
    s1, s2 = min(s1, s2), max(s1, s2)

    if step%2 == 0:
        return (
            f20(s1 + 1, s2, step + 1) and
            f20(s1 + 2, s2, step + 1) and
            f20(s1*2, s2, step + 1)
        )
    
    return (
            f20(s1 + 1, s2, step + 1) or
            f20(s1 + 2, s2, step + 1) or
            f20(s1*2, s2, step + 1)
        )


print("Zadacha 20")
res = []
for s2 in range(1, 68 + 1):
    if f20(12, s2):
        res.append(s2)

print(min(res), max(res))



def f21(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 > 80) and (step in (3, 5)): return True
    elif (
        ((s1 + s2 <= 80) and (step == 5)) or
        (s1 + s2 > 80)
    ): return False


    # s1 - min, s2 - max VSEGDA
    s1, s2 = min(s1, s2), max(s1, s2)

    if step%2 == 1:
        return (
            f21(s1 + 1, s2, step + 1) and
            f21(s1 + 2, s2, step + 1) and
            f21(s1*2, s2, step + 1)
        )
    
    return (
            f21(s1 + 1, s2, step + 1) or
            f21(s1 + 2, s2, step + 1) or
            f21(s1*2, s2, step + 1)
        )


print("Zadacha 21")
res = []
for s2 in range(1, 68 + 1):
    if f21(12, s2):
        res.append(s2)

print(max(res))