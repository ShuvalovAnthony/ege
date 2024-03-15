import sys
from functools import lru_cache

sys.setrecursionlimit(15000)


@lru_cache
def f(n):
    if n >= 2024: return 1
    return f(n + 2) + f(n + 4)


res = set()

for i in range(1, 10**4):
    res.add(f(i))

print(len(res))