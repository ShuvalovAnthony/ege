def f(a, b):
    if (a > b) or a == 15: return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a + 2, b)

print(f(3, 9)*f(9, 20))