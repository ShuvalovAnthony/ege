def f(start, stop):
    if start == stop: return 1
    elif start > stop: return 0

    return f(start + 1, stop) + f(start*2, stop)


print(
    f(2, 11)*f(11, 25)*f(25, 50)
)