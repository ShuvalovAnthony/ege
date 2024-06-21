import sys

sys.setrecursionlimit(15000)
sys.set_int_max_str_digits(100000)

def f(n):
    if n == 1: return 1
    return (n + 1)*f(n - 1)


print((f(2024) - 3*f(2023))//f(2022))