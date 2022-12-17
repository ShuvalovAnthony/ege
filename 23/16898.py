def f(a, b):
    if (a > b) or (a in (5, 10)): return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a*2, b) + f(a + 3, b)


print(f(2, 14))