def f(n):
    # n == 1 or n == 2 тоже самое
    if n in (1, 2): return 5
    return 5*f(n - 1) - 4*f(n - 2)


print(f(13))