def f(start, stop):
    if start == stop: return True
    elif start > stop or start == 81: return False

    return (
        f(start + int(str(start)[0]), stop) +
        f(start + 3, stop) +
        f(start*2 - 1, stop)
    )


print(f(42, 73)*f(73, 89))