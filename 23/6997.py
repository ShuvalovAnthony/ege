def f(start, stop=15):
    if start > stop: return 0
    elif start == stop: return 1
    return f(start + 1) +\
    f(start*2) + \
    f(start*2 + 1) +\
    f(start*10)


print(f(1))





