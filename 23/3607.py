def f(a, b): # a - входное число b - конечное
    if a > b: return 0
    elif a == b: return 1
    return f(a + 2, b) + f(a*5, b)


print(f(2, 50))



