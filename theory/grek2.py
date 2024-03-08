from functools import lru_cache

primes = []

@lru_cache
def prime(n):
    for i in range(2, int(n**0.5)):
        if n%i == 0: return False
    return True



for i in range(3, 10**18 + 1, 2):
    print(i)
    if prime(i):
        primes.append(i)


print(primes)