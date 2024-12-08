from functools import lru_cache
import sys


sys.setrecursionlimit(5000)

@lru_cache(256)
def f(n):
    if n < 11: return 10
    return n + f(n - 1)


print(f(2024) - f(2022))


counter = 0

def f(n):
    if n == 0: return 0
    if n%2 == 0: return f(n/2)
    return 1 + f(n - 1)


def check(n):
    return f(n) == 3


for n in range(1, 1000 + 1):
    counter += check(n)


print(counter)