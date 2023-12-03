from functools import lru_cache


counter = 0

@lru_cache
def f(n):
    if n < 9: return n
    return f(n//9) + f(n%9)



for n in range(4*6**20, 5*6**20 + 1):
    if f(n) == 121:
        counter += 1
        print(n)