def f19(s1, s2):
    s1, s2 = min(s1, s2), max(s1, s2)
    if (s1 + s1 + s2 > 39): return 1
    return 0

res = []

for s1 in range(1, 50):
    for s2 in range(1, 50):
        if f19(s1, s2):
            res.append(s1 + s2)

print(min(res))
            
print('-'*10)


def f20(s1, s2, step=1): # 1p 2v 3p 4v
    if (s1 + s2 > 39) and (step == 4): return 1
    elif (
        (s1 + s2 > 39) or
        (s1 + s2 <= 39) and (step == 4)
    ): return 0

    s1, s2 = min(s1, s2), max(s1, s2)
    if step%2:
        res = []
        for i in range(1, s1 + 1):
            res.append(f20(s1 + i, s2, step + 1))
        return any(res)

    res = []
    for i in range(1, s1 + 1):
        res.append(f20(s1 + i, s2, step + 1))
    return all(res)

s2_list = []

for s2 in range(1, 36):
    if f20(4, s2): s2_list.append(s2)


print(min(s2_list), max(s2_list))


print('-'*10)


def f21(s1, s2, step=1): # 1p 2v 3p 4v
    if (s1 + s2 > 39) and (step == 5): return 1
    elif (
        (s1 + s2 > 39) or
        (s1 + s2 <= 39) and (step == 5)
    ): return 0

    s1, s2 = min(s1, s2), max(s1, s2)
    if step%2 == 0:
        res = []
        for i in range(1, s1 + 1):
            res.append(f21(s1 + i, s2, step + 1))
        return any(res)

    res = []
    for i in range(1, s1 + 1):
        res.append(f21(s1 + i, s2, step + 1))
    return all(res)


for s2 in range(1, 36):
    if f21(4, s2):
        print(s2)
        break