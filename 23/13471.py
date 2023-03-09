def f(a, b):
    if (a > b) or (a == 24): return 0
    elif a == b: return 1
    return f(a + 1, b) + f(2*a + 1, b)


print(f(1, 25))