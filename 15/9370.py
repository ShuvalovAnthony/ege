def p(x):
    return 5 <= x <= 54


def q(x):
    return 50 <= x <= 93


for a in range(-50, 150):
    count = 0

    for x in range(-50, 150):
        if not (
            ((not p(x)) and q(x)) <= (x > a)
        ):
            count += 1


    if count == 20:
        print(a)
