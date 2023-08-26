def f(start, stop): # start - входное число stop - конечное
    if (start > stop): return 0
    elif start == stop: return 1
    return f(start + 2, stop) + f(start*5, stop)


print(f(2, 50))