def f(a, b):
    if a > b: return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a + 2, b) + f(a + 3, b)

print(f(1, 8)*f(8, 15))