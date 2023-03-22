def f19(kuchi: list, step:int=1): # 1p 2v 3p 4v 5p [5, 10, 15, 20, 25]
    if (sum(kuchi) >= 97) and (step == 3): return 1
    elif (
        (sum(kuchi) >= 97) or
        (sum(kuchi) < 97) and (step == 3)
    ): return 0
    res = []
    for add in (1, 3, 5, 7, 8, 12):
        for i in range(len(kuchi)): 
            tmp = kuchi.copy()
            tmp[i] += add
            res.append(f19(tmp, step + 1))
    
    if step%2 == 0:
        return all(res)
    return any(res)


for s in range(1, 20):
    for m in range(2, 21):
        kuchi = []
        for i in range(1, s + 1):
            kuchi.append(i*m)
        if f19(kuchi):
            print(s)


print('-'*10)


def f20(kuchi, step:int=1): # 1p 2v 3p 4v 5p
    if (sum(kuchi) >= 97) and (step == 2): return 1
    elif (
        (sum(kuchi) >= 97) or
        (sum(kuchi) < 97) and (step == 2)
    ): return 0
    res = []
    for add in (1, 3, 5, 7, 8, 12):
        for i in range(len(kuchi)):
            tmp = kuchi.copy()
            tmp[i] += add
            res.append(f20(tmp, step + 1))
    
    if step%2 == 0:
        return all(res)
    return any(res)


for s in range(1, 20):
    for m in range(2, 21):
        kuchi = []
        for i in range(1, s + 1):
            kuchi.append(i*m)
        if f20(kuchi):
            print(s)

print('-'*10)

def f21(kuchi, step:int=1): # 1p 2v 3p 4v 5p
    if (sum(kuchi) >= 97) and (step == 4): return 1
    elif (
        (sum(kuchi) >= 97) or
        (sum(kuchi) < 97) and (step == 4)
    ): return 0
    res = []
    for add in (1, 3, 5, 7, 8, 12):
        for i in range(len(kuchi)):
            tmp = kuchi.copy()
            tmp[i] += add
            res.append(f21(tmp, step + 1))
    
    if step%2 == 0:
        return all(res)
    return any(res)


for s in range(1, 20):
    for m in range(2, 21):
        kuchi = []
        for i in range(1, s + 1):
            kuchi.append(i*m)
        if f21(kuchi):
            print(s)

print('-'*10)