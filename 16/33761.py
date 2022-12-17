def f(n):
    if n == 0: return 0
    elif n%2 == 0: return f(n//2)
    return 1 + f(n - 1)



for n in range(0, 10**9):
    if f(n) == 11:
        print(n)
        break