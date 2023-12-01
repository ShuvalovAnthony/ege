print('zadacha 21')

def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 <= 40) and (step in (3, 5)): return 1
    elif (
        (step == 5 and (s1 + s2 > 40)) or
        (step < 5 and (s1 + s2 <= 40))
    ): return 0

    if step%2 == 0:
        return (
            f(s1 - 1, s2, step + 1) or
            f((s1 + 1)//2, s2, step + 1) or
            f(s1, s2 - 1, step + 1) or
            f(s1, (s2 + 1)//2, step + 1)
        )
    return (
            f(s1 - 1, s2, step + 1) and
            f((s1 + 1)//2, s2, step + 1) and
            f(s1, s2 - 1, step + 1) and
            f(s1, (s2 + 1)//2, step + 1)
        )

for s2 in range(100, 20, -1):
    if f(20, s2):
        print(s2)
        break
