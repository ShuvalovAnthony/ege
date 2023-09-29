from functools import lru_cache

@lru_cache
def f(n):
    if n == 0: return 1
    if n%2: return 1 + f(n - 1)
    return f(n//2)



counter = 0

for i in range(1, 5*10**8 + 1):
    if f(i) == 3: counter += 1


print(counter)