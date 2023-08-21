from functools import lru_cache

@lru_cache
def fib(n: int): # n = 6
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


for i in range(1, 1000):
    print(i, fib(i))