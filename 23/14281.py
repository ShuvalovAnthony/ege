def f(a, b): # a - начальное число, b - число к которому стремимся
    if a > b: return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a + 2, b)

print(f(1, 11))