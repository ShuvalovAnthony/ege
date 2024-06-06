# ОБЯЗАТЕЛЬНО 9 но НЕЛЬЗЯ 10
# ЛИБО ОБЯЗАТЕЛЬНО 10 но НЕЛЬЗЯ 9

def f1(a, b):
    if (a > b) or (a == 10): return 0
    elif a == b: return 1
    return f1(a + 1, b) + f1(a + 2, b)


def f2(a, b):
    if (a > b) or (a == 9): return 0
    elif a == b: return 1
    return f2(a + 1, b) + f2(a + 2, b)


print(f1(3, 9)*f1(9, 20) + f2(3, 10)*f2(10, 20))