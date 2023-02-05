def p(x):
    return 19 <= x <= 84


def q(x):
    return 4 <= x <= 51


def a(start, stop, x):
    return start <= x <= stop

answ = 10**6

for start in range(-200, 200):
    for stop in range(-200, 200):
        flag = True
        for x in range(-200, 200):
            if not ((not q(x)) or p(x) or a(start, stop, x)):
            # if not ((not q(x)) or (p(x) or (not (q(x) and (not a(start, stop, x)))))):
                flag = False
                break

        if flag:
            if abs(start - stop) <= answ:
                answ = abs(start - stop)
                res = (start, stop)
            

print(answ + 1, res)