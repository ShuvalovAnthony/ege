# 19

def f(s, step=1): # 1p 2v 3p 4v 5p
    if s >= 36 and s <= 60:
        if step == 3: return 1
        else: return 0
    elif s >= 36 and s > 60:
        if step == 2: return 1
        else: return 0
    
    if step%2 == 0:
        return f(s + 1, step + 1) or \
            f(s*2, step + 1) or \
            f(s*3, step + 1)
    
    return f(s + 1, step + 1) and \
           f(s*2, step + 1) and \
           f(s*3, step + 1)


for s in range(1, 100):
    if f(s):
        print(s)



def f(s, step=1): # 1p 2v 3p 4v 5p
    if s >= 36 and s <= 60:
        if step == 4: return 1
        else: return 0
    elif s >= 36 and s > 60:
        if step == 3: return 1
        else: return 0
    
    if step%2 != 0:
        return f(s + 1, step + 1) or \
            f(s*2, step + 1) or \
            f(s*3, step + 1)
    
    return f(s + 1, step + 1) and \
           f(s*2, step + 1) and \
           f(s*3, step + 1)

counter = 0

for s in range(1, 20):
    counter += f(s)

print(counter)


def f(s, step=1): # 1p 2v 3p 4v 5p
    if s >= 36 and s <= 60:
        if step in (3, 5): return 1
        else: return 0
    elif s >= 36 and s > 60:
        if step in (2, 4): return 1
        else: return 0
    
    if step%2 == 0:
        return f(s + 1, step + 1) or \
            f(s*2, step + 1) or \
            f(s*3, step + 1)
    
    return f(s + 1, step + 1) and \
           f(s*2, step + 1) and \
           f(s*3, step + 1)

for s in range(1, 35):
    if f(s): print(s)
