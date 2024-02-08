def f21(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 82) and (step in (3, 5)): return True
    elif (
        ((s1 + s2 < 82) and (step == 5)) or
        (s1 + s2 >= 82)
    ): return False

    if step%2 == 1:
        return (
            f21(s1 + 1, s2, step + 1) and
            f21(s1*4, s2, step + 1) and
            f21(s1, s2 + 1, step + 1) and
            f21(s1, s2*4, step + 1)
        )

    return (
            f21(s1 + 1, s2, step + 1) or
            f21(s1*4, s2, step + 1) or
            f21(s1, s2 + 1, step + 1) or
            f21(s1, s2*4, step + 1)
        )


print("Zadacha 21")
for s2 in range(1, 77 + 1):
    if f21(4, s2):
        print(s2)
        break