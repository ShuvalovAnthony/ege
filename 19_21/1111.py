def f(h1, h2, step): #p-1, b-2, p-3, b-4
    if (h1 + h2 >= 231) and (step in (3, 5)):
        return True
    elif (
            ((h1 + h2 < 231) and (step == 5)) or
            ((h1 + h2 >= 231))
    ):
        return False
    
    if step%2 != 0:
        return (
                f(h1 + 4, h2, step + 1) and
                f(h1, h2 + 4, step + 1) and
                f(h1, h2 * 3, step + 1) and
                f(h1 * 3, h2, step + 1)
        )
    return (
        f(h1 + 4, h2, step + 1) or
        f(h1, h2 + 4, step + 1) or
        f(h1, h2 * 3, step + 1) or
        f(h1 * 3, h2, step + 1)
    )

s = []
for h2 in range(1, 218):
    if f(10, h2, 1):
        s.append(h2)


print(sorted(s))