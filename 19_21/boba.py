def f(s1, s2, step=1): # 1p 2v 3p 4v 5p 6v proverka na 3 / 5
    if (s1 + s2 >= 30) and (step in (3, 5)): return 1
    elif (s1 + s2 < 30 and step == 5) or\
        (s1 + s2 >= 30 and step < 5): return 0

    if step%2: # petya
        return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and\
            f(s1*2, s2, step + 1) and f(s1, s2*2, step + 1)
    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
            f(s1*2, s2, step + 1) or f(s1, s2*2, step + 1)
    

print('zadazha 21')
for s1 in range(1, 30):
    for s2 in range(1, 30):
        if f(s1, s2):
            print(s1, s2)