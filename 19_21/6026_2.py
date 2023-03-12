# s1 - количество камней в первой куче
# s2 - кол-во камней во 2ой куче
# step - номер шага/хода

def f19(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 117) and (step == 3): return 1
    elif (
        ((s1 + s2 < 117) and (step == 3)) or
        ((s1 + s2 >= 117) and (step < 3))
    ): return 0

    return f19(s1 + 1, s2, step + 1) or\
    f19(s1*2, s2, step + 1) or\
    f19(s1, s2 + 1, step + 1) or\
    f19(s1, s2*2, step + 1)

for s2 in range(1, 104):
    if f19(13, s2):
        print(s2)
        break
        

print('-----')

def f20(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 117) and (step == 4): return 1
    elif (
        ((s1 + s2 < 117) and (step == 4)) or
        ((s1 + s2 >= 117) and (step < 4))
    ): return 0

    if step%2 == 0: # ХОДЫ ВАНИ!!!
        return f20(s1 + 1, s2, step + 1) and\
        f20(s1*2, s2, step + 1) and\
        f20(s1, s2 + 1, step + 1) and\
        f20(s1, s2*2, step + 1)

    return f20(s1 + 1, s2, step + 1) or\
    f20(s1*2, s2, step + 1) or\
    f20(s1, s2 + 1, step + 1) or\
    f20(s1, s2*2, step + 1)

for s2 in range(1, 104):
    if f20(13, s2):
        print(s2)


print('-----')


def f21(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 117) and (step in (3, 5)): return 1
    elif (
        ((s1 + s2 < 117) and (step == 5)) or
        ((s1 + s2 >= 117) and (step not in (3, 5)))
    ): return 0

    if step%2: # ХОДЫ ПЕТИ!!!
        return f21(s1 + 1, s2, step + 1) and\
        f21(s1*2, s2, step + 1) and\
        f21(s1, s2 + 1, step + 1) and\
        f21(s1, s2*2, step + 1)

    return f21(s1 + 1, s2, step + 1) or\
    f21(s1*2, s2, step + 1) or\
    f21(s1, s2 + 1, step + 1) or\
    f21(s1, s2*2, step + 1)

for s2 in range(1, 104):
    if f21(13, s2):
        print(s2)
        break