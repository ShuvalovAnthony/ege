def f(a, b, double_mult=False): # a - начальное число, b - число к которому стремимся
    if a > b: return 0
    elif a == b: return 1
    if double_mult:
        return f(a + 1, b, double_mult=False) + f(a + 2, b, double_mult=False)
    return f(a + 1, b) + f(a + 2, b) + f(a*2, b, True) 




print(f(1, 11))