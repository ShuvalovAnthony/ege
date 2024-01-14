def f(start, stop):
    if start == stop: return 1
    elif start > stop or start == 9: return 0

    return (
        f(start + 2, stop) + 
        f(start + 3, stop) +
        f(start*3, stop)
    )


print(f(3, 15)*f(15, 25))