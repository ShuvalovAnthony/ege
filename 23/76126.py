def f(start, stop, check):
    if (start == 8) or (start == 20): check += 1
    if (start < stop) or (check > 1): return 0
    if start == stop: return 1

    return sum([
        f(start - 1, stop, check),
        f(start - 3, stop, check),
        f(start//2, stop, check),
    ])


print(f(31, 3, 0))