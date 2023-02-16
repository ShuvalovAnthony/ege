def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 117) and (step == 3): return 1
    elif ((s1 + s2 >= 117) and (step != 3)) or \
        ((s1 + s2 < 117) and (step == 3)): return 0
    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or \
        f(s1*2, s2, step + 1) or f(s1, s2*2, step + 1)

print('Номер 19')
for s2 in range(1, 104):
    if f(13, s2):
        print(s2)
        break


def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 117) and (step == 4): return 1
    elif ((s1 + s2 >= 117) and (step < 4)) or \
        ((s1 + s2 < 117) and (step == 4)): return 0
    if not step%2:
        return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and \
        f(s1*2, s2, step + 1) and f(s1, s2*2, step + 1)
    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or \
        f(s1*2, s2, step + 1) or f(s1, s2*2, step + 1)

print('Номер 20')
for s2 in range(1, 104):
    if f(13, s2):
        print(s2)


def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 117) and (step in (3, 5)): return 1
    elif ((s1 + s2 >= 117) and (step < 5)) or \
        ((s1 + s2 < 117) and (step == 5)): return 0
    if not step%2:
        return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or \
        f(s1*2, s2, step + 1) or f(s1, s2*2, step + 1)
    return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and \
        f(s1*2, s2, step + 1) and f(s1, s2*2, step + 1)

print('Номер 21')
for s2 in range(1, 104):
    if f(13, s2):
        print(s2)