def f(n):
    if n == 0: return 0
    elif n%3 == 0: return n + f(n - 3)
    else: return n + f(n - n%3)


print(f(26))

# a mod b ===== a%b
