from functools import lru_cache
import sys


sys.setrecursionlimit(5000)

@lru_cache
def f(n):
    if n < 11: return 10
    return n + f(n - 1)


print(f(2204) - f(2202))





# @lru_cache
# def fib(n):
#     if n <= 2: return 1
#     return fib(n - 1) + fib(n - 2)


# for i in range(1, 200):
#     print(i, 'ое число Фибо =', fib(i))


