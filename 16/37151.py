def f(n: int):
    if n <= 1: return 0
    elif n%2 == 1: return f(n - 1) + 3*n**2
    return n//2 + f(n - 1) + 2



print(f(49))

