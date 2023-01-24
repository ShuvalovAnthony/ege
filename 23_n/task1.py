def f(a, b, flag1=False, flag2=False):
    if a > b: return 0
    elif a == b: return 1
    if flag1:
        return f(a*2, b, flag1=True)
    elif flag2:
        return f(a + 1, b, flag2=True)
    return f(a + 1, b) + f(a*2, b)

print(f(1, 14))
