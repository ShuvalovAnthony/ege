def f(s, step=1): #1p 2v 3p 4v 5p
    if (step == 5) and (s >= 26): return 1
    elif (step == 5) and (s < 26): return 0
    if s%2:
        if step%2: # petya
            return f(s + 1, step + 1) and\
            f(s + 2, step + 1) and\
            f(s*2, step + 1)
        else:
            return f(s + 1, step + 1) or\
            f(s + 2, step + 1) or\
            f(s*2, step + 1)
    else:
        if step%2: # petya
            return f(s + 1, step + 1) and\
            f(s + 2, step + 1)
        else:
            return f(s + 1, step + 1) or\
            f(s + 2, step + 1)
        

for s in range(1, 26):
    if f(s): print(s)
