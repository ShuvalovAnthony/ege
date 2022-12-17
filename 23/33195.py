def f(a, b):
    if (a > b) or (a == 10) or (a == 11): return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a + 2, b) + f(a*3, b)



# 1 -> 8-> 27

print(f(1, 8)*f(8, 27))