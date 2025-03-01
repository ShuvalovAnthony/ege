from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)


@lru_cache
def fib(n: int):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


for i in range(1, 100):
    print(i, fib(i))


