def f19(s1, s2, step=1): # 1p 2v 3p 4v 5p
    if (s1 + s2 >= 77) and (step == 3): return 1
    elif (s1 + s2 >= 77) or (step > 3): return 0

    if step%2:
        return f19(s1 + 1, s2, step + 1) or \
        f19(s1*2, s2, step + 1) or \
        f19(s1, s2 + 1, step + 1) or \
        f19(s1, s2*2, step + 1)
    
    return f19(s1 + 1, s2, step + 1) or \
        f19(s1*2, s2, step + 1) or \
        f19(s1, s2 + 1, step + 1) or \
        f19(s1, s2*2, step + 1)


for s2 in range(1, 70):
    if f19(7, s2):
        print(s2)
        break