def a(x, start, stop):
    return start <= x <= stop


def q(x):
    return 22 <= x <= 57


def p(x):
    return 17 <= x <= 46


min_dist = 10000

for start in range(16, 60):
    for stop in range(16, 60):
        flag = True
        for x in range(16, 60):
            if not (a(x, start, stop) or (not p(x)) or (not q(x))):
                flag = False
                break

        if flag:
            min_dist = min(min_dist, stop - start)

print(min_dist)