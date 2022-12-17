def f(a, b):
    if a > b: return 0
    elif a == b: return 1
    return f(a + 1, b) + f(a*2, b)


# 3 -> 13 -> 30-> 60

print(f(3, 13)*f(13, 30)*f(30, 60))