def p(x):
    return 23 <= x <= 58


def q(x):
    return 1 <= x <= 39


def a(start, stop, x):
    return start <= x <= stop

min_dlina = 10**6

for start in range(-100, 100):
    for stop in range(-100, 100):
        flag = True
# ((x ∈ P) ∨ (x ∈ А)) → ((x ∈ Q) ∨ (x ∈ А))
        for x in range(-100, 100):
            if not ((p(x) or a(start, stop, x)) <= (q(x) or a(start, stop, x))):
                flag = False
                break

        if flag and abs(start - stop) < min_dlina:
            min_dlina = abs(start - stop)
            coords = (start, stop)


print(min_dlina, coords)