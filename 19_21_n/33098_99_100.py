def f(s1, s2, step=1): # 1p 2v 3p 4v
    if (s1 + s2 >= 45) and (step == 3): return 1
    elif (s1 + s2 < 45 and step == 3) or\
        (s1 + s2 >= 45 and step < 3): return 0

    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
        f(s1*3, s2, step + 1) or f(s1, s2*3, step + 1)

print('zadacha 19')
for s2 in range(1, 41):
    if f(4, s2): 
        print(s2)
        break



def f(s1, s2, step=1): # 1p 2v 3p 4v
    if (s1 + s2 >= 45) and (step == 4): return 1
    elif (s1 + s2 < 45 and step == 4) or\
        (s1 + s2 >= 45 and step < 4): return 0

    if step%2: # нечетный шаг PETYA
        return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
            f(s1*3, s2, step + 1) or f(s1, s2*3, step + 1)
    return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and\
            f(s1*3, s2, step + 1) and f(s1, s2*3, step + 1)


print('zadacha 20')
for s2 in range(1, 41):
    if f(4, s2): 
        print(s2)




def f(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 45) and (step in (3, 5)): return 1
    elif (s1 + s2 < 45 and step == 5) or\
        (s1 + s2 >= 45 and step < 5): return 0

    if step%2: # нечетный шаг PETYA
        return f(s1 + 1, s2, step + 1) and f(s1, s2 + 1, step + 1) and\
            f(s1*3, s2, step + 1) and f(s1, s2*3, step + 1)
    return f(s1 + 1, s2, step + 1) or f(s1, s2 + 1, step + 1) or\
            f(s1*3, s2, step + 1) or f(s1, s2*3, step + 1)


print('zadacha 21')
for s2 in range(1, 41):
    if f(4, s2): 
        print(s2)




