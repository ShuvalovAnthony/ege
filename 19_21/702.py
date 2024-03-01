def f19(s, step=1): # 1p 2v 3p 4v 5p
    if (s >= 36):
        if (s <= 85):
            print("<85", step - 1)
            return step - 1
        else:
            print(">85", step)
            return step
        
    moves = [f19(s + 2, step + 1), f19(s*3, step + 1)]

    # %2 == 0 - V, != 0 - P
    if step%2 != 0: return any(moves)
    return all(moves)



print(f19(32))