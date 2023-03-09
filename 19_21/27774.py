def f(s1, s2, step=1):
    if (s1 + s2 <= 20) and (step == 3): return 1
    elif ((s1 + s2 > 20) and (step == 3)) or \
    ((s1 + s2 <= 20) and (step < 3)): return 0
    return f(s1 - 1, s2, step + 1) or f(s1, s2 - 1, step + 1) or \
        f((s1 // 2) + (s1 % 2), s2, step + 1) or f(s1, (s2 // 2) + (s2 % 2), step + 1)

for i in range(11, 100):
    if f(10, i):
        print(i)
