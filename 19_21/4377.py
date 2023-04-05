def f19(s, step=1): #1p 2v 3p 4v 5p
    if (step in (3, 5)) and (s >= 26): return 1
    elif (
        ((step == 5) and (s < 26)) or
        (s >= 26)
        ): return 0
    if s%2:
        if step%2: # petya
            return f19(s + 1, step + 1) and\
            f19(s + 2, step + 1) and\
            f19(s*2, step + 1)
        else:
            return f19(s + 1, step + 1) or\
            f19(s + 2, step + 1) or\
            f19(s*2, step + 1)
    else:
        if step%2: # petya
            return f19(s + 1, step + 1) and\
            f19(s + 2, step + 1)
        else:
            return f19(s + 1, step + 1) or\
            f19(s + 2, step + 1)
        

for s in range(1, 26):
    if f19(s): print(s)


print('-'*20)

def f20(s, step=1): # 1p 2v 3p 4v 5p
    if (step == 4) and (s >= 26): return 1
    elif (
        ((step == 4) and (s < 26)) or
        (s >= 26)
        ): return 0
    if s%2:
        if step%2 == 0: # petya
            return f20(s + 1, step + 1) and\
            f20(s + 2, step + 1) and\
            f20(s*2, step + 1)
        else:
            return f20(s + 1, step + 1) or\
            f20(s + 2, step + 1) or\
            f20(s*2, step + 1)
    else:
        if step%2 == 0: # petya
            return f20(s + 1, step + 1) and\
            f20(s + 2, step + 1)
        else:
            return f20(s + 1, step + 1) or\
            f20(s + 2, step + 1)
        

for s in range(1, 26):
    if f20(s): print(s)
