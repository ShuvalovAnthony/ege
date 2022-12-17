def p(x):
    return 69 <= x <= 91


def q(x):
    return 77 <= x <= 114


def a(start, stop, x):
    return start <= x <= stop


answ = 10**6
# ¬P ∨ ¬(P ≡ Q) ∨ ¬Q ∨ A


for start in range(-150, 150):
    for stop in range(-150, 150):
        flag = True
        for x in range(-150, 150):
            if not ((not p(x)) or (p(x) != q(x)) or (not q(x)) or a(start, stop, x)):
                flag = False
                break
        
        if flag:
            if abs(start - stop) < answ:
                answ = abs(start - stop)
                res = (start, stop)

print(answ, res)


