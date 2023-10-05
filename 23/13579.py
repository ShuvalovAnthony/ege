def f(start, stop):
    if start > stop: return 0
    elif start == stop: return 1
    return sum(f(start + i, stop) for i in (1, 2, 3))


print(f(1, 8)*f(8, 15))