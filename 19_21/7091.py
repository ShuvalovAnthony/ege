def f(s1, step=1): # 1p 2v 3p 4v 5p 6v 7p
    if (s1 >= 443) and (step == 3): return 1
    elif ((s1  >= 443) and (step < 3)) or (step > 3): return 0

    if step%2:
        return f(s1 + 1, step + 1) and f(s1 + 3, step + 1) and f(s1*2, step + 1)
    return f(s1 + 1, step + 1) or f(s1 + 3, step + 1) or f(s1*2, step + 1)
    

for s in range(1, 442):
    if f(s):
        print(s)