def f(n):
    if n >= 2000: return 2000
    elif n%2: return n*f(n + 1)
    return n*f(n + 1)//2


print(f(1998)/f(2001))