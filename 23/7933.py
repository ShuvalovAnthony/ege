def f(a, b):
    if a > b: return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a + 2, b) + f(2*a - 1, b)# a + a - 1


print(f(2, 9))



