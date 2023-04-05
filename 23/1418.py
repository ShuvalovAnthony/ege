def f(a, b):
    if a == b: return 1
    elif (a > b) or (a == 60): return 0
    return f(a + 5, b) + f(a*5, b)


print(f(5, 30)*f(30, 280))