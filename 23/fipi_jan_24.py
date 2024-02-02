def f(start, stop): # start - входное число stop - конечное
    if (start > stop) or start == 11: return 0
    elif start == stop: return 1
    return f(start + 1, stop) + f(start*2, stop) + f(start**2, stop)


print(f(2, 20))