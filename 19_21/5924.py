def f(s1, step=1): # 1p 2v 3p 4v 5p 6v 7p
    if (s1 >= 56) and (step == 7): return 1
    elif ((s1  >= 56) and (step < 7)) or ((s1 < 56) and (step == 7)): return 0

    if step%2:
        if s1%3: return f(s1 + 1, step + 1) and f(s1 + 2, step + 1)
        return f(s1 + 1, step + 1) and f(s1 + 2, step + 1) and f(s1*3, step + 1)
    
    if s1%3: return f(s1 + 1, step + 1) or f(s1 + 2, step + 1)
    return f(s1 + 1, step + 1) or f(s1 + 2, step + 1) or f(s1*3, step + 1)
    

for s in range(1, 56):
    if f(s):
        print(s)