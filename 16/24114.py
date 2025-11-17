from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(50000)
def g(n):
    if n >= 30000: return 3
    return (g(n + 3) + 7)
def f(n):
    return g(n + 1)
print(g(1501))