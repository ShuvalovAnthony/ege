def f19(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 464) and (step == 3): return True
    elif (
        ((h1 + h2 < 464) and (step == 3)) or
        (h1 + h2 >= 464)
        ): return False
    
    moves = [f19(h1 + 2, h2, step + 1), 
            f19(h1*3, h2, step + 1), 
            f19(h1, h2 + 2, step + 1), 
            f19(h1, h2*3, step + 1)]
    
    return any(moves)


for s2 in range(1, 451):
    if f19(13, s2):
        print(s2)
        break


def f20(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 464) and (step == 4): return True
    elif (
        ((h1 + h2 < 464) and (step == 4)) or
        (h1 + h2 >= 464)
        ): return False
    
    moves = [f20(h1 + 2, h2, step + 1), 
            f20(h1*3, h2, step + 1), 
            f20(h1, h2 + 2, step + 1), 
            f20(h1, h2*3, step + 1)]

    if step%2: return any(moves)
    return all(moves)

print('-------')
answ = []
for s2 in range(1, 451):
    if f20(13, s2):
        answ.append(s2)

print(*answ[:2])



def f21(h1, h2, step=1): # 1p 2v 3p 4v 5p
    if (h1 + h2 >= 464) and (step in (3, 5)): return True
    elif (
        ((h1 + h2 < 464) and (step == 5)) or
        (h1 + h2 >= 464)
        ): return False
    
    moves = [f21(h1 + 2, h2, step + 1), 
            f21(h1*3, h2, step + 1), 
            f21(h1, h2 + 2, step + 1), 
            f21(h1, h2*3, step + 1)]

    if step%2 == 0: return any(moves)
    return all(moves)

print('-------')

for s2 in range(1, 451):
    if f21(13, s2):
        print(s2)
        break
