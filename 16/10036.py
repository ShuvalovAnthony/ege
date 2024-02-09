from functools import lru_cache

@lru_cache
def f(n):
    if n < 3: return n
    return (2*n - 1)*(f(n - 1) + f(n - 2))


num = 10**9 + 7


print(f(69)%num)