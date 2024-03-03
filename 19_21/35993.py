def f19(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 79) and (step == 3): return True
    elif (
        ((s1 + s2 >= 79) and (step < 3)) or
        ((s1 + s2 < 79) and (step == 3))
    ): return False

    return (
        f19(s1 + 1, s2, step + 1) or
        f19(s1*3, s2, step + 1) or
        f19(s1, s2 + 1, step + 1) or
        f19(s1, s2*3, step + 1)
    )

print("19 -------")
for s2 in range(1, 72 + 1):
    if f19(6, s2):
        print(s2)
        break



def f20(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 79) and (step == 4): return True
    elif (
        ((s1 + s2 >= 79) and (step < 4)) or
        ((s1 + s2 < 79) and (step == 4))
    ): return False

    if step%2 == 1:
        return (
            f20(s1 + 1, s2, step + 1) or
            f20(s1*3, s2, step + 1) or
            f20(s1, s2 + 1, step + 1) or
            f20(s1, s2*3, step + 1)
        )
    
    return (
            f20(s1 + 1, s2, step + 1) and
            f20(s1*3, s2, step + 1) and
            f20(s1, s2 + 1, step + 1) and
            f20(s1, s2*3, step + 1)
        )


print("20 -------")
for s2 in range(1, 72 + 1):
    if f20(6, s2):
        print(s2)




def f21(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 79) and (step == 3): return True
    elif (
        ((s1 + s2 >= 79) and (step < 3)) or
        ((s1 + s2 < 79) and (step == 3))
    ): return False

    if step%2 == 0:
        return (
            f21(s1 + 1, s2, step + 1) or
            f21(s1*3, s2, step + 1) or
            f21(s1, s2 + 1, step + 1) or
            f21(s1, s2*3, step + 1)
        )
    
    return (
            f21(s1 + 1, s2, step + 1) and
            f21(s1*3, s2, step + 1) and
            f21(s1, s2 + 1, step + 1) and
            f21(s1, s2*3, step + 1)
        )


print("21 -------")
for s2 in range(1, 72 + 1):
    if f21(6, s2):
        print(s2)
