def f19(s1, s2, step=1): # 1p, 2v, 3p, 4v, 5p
    if (max(s1, s2) >= 50):
        if (s1 + s2) <= 109:
            if step == 4: return True
            else: return False
        else:
            if step == 3: return True
            else: return False
            
    elif (
        ((step == 2) and (max(s1, s2) >= 50))
        or (step > 4)
    ): return False
    
    moves = [f19(s1 + 1, s2, step + 1), f19(s1, s2 + 1, step + 1),
            f19(s1 + 2, s2, step + 1), f19(s1, s2 + 2, step + 1),
            f19(s1*2, s2, step + 1), f19(s1, s2*2, step + 1)]
    
    if step%2 == 0:
        return all(moves)
    
    if step == 1:
        if f19(s1 + 1, s2, step + 1) or f19(s1, s2 + 1, step + 1):
            return 'А'
        elif f19(s1 + 2, s2, step + 1) or f19(s1, s2 + 2, step + 1):
            return 'Б'
        elif f19(s1*2, s2, step + 1) or f19(s1, s2*2, step + 1):
            return 'В'
    
    return any(moves)

    


for s2 in range(1, 50):
    if f19(24, s2):
        print(s2, f19(24, s2))