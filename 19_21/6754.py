def f19(s1, step=1):
    if (s1 >= 351) and (step == 3): return 1
    elif (
        ((s1 >= 351) and (step < 3) )or 
        ((s1 < 351) and (step == 3))
        ): return 0
    
    if step%2 == 0:
        return f19(s1 + 1, step + 1) and\
            f19(s1 + 4, step + 1) and\
            f19(s1*2, step + 1) 


    return f19(s1 + 1, step + 1) or\
        f19(s1 + 4, step + 1) or\
        f19(s1*2, step + 1) 


for s1 in range(1, 351):
    if f19(s1):
        print(s1)