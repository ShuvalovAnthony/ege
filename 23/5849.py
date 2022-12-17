from functools import lru_cache


@lru_cache
def f(a, b):
    if a > b: return 0
    elif a == b: return 1
    c = str(a)
    c = int(str(int(c[0]) + 1) + c[1::])
    return f(a + 1, b) + f(a + 10, b)


print(f(35, 301))