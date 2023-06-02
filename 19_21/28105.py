def ff(s, step=1):
    if (step == 4) and (s >= 40):
        return 1
    elif ((step == 4) and (s < 40)) or (s >= 40):
        return 0

    if step%2: return ff(s + 1, step + 1) or ff(s*3 - 2, step + 1)
    else: return ff(s + 1, step + 1) and ff(s*3 - 2, step + 1)

for s in range(2, 40):
    if ff(s, 1):
        print(s)

print('-'*20)


def f(s, step=1):
    if (s > 39) and (step == 4):
        return 1
    elif ((step == 4) and (s < 40)) or (s > 39):
        return 0
    
    if s%2:
        return f(s + 1, step + 1) or f(s*3 - 2, step + 1)
    else:
        return f(s + 1, step + 1) and f(s*3 - 2, step + 1)

for s in range(2, 40):
    if f(s):
        print(s)