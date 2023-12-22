def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 82) and (step == 3):
        return True
    elif (
        ((h1 + h2 >= 82) and (step < 3)) or
        ((h1 + h2 < 82) and (step == 3))
    ): return False

    return (
        f19(h1 + 1, h2, step + 1) or
        f19(h1*4, h2, step + 1) or
        f19(h1, h2 + 1, step + 1) or
        f19(h1, h2*4, step + 1)
    )


for h2 in range(1, 78):
    if f19(4, h2):
        print(h2)
        break