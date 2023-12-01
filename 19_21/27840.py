def f(s, step=1): # s - колво камней, step - шаг
    if s >= 65 and step in (3, 5):
        return 1
    elif (step == 5 and s < 65) or (step < 5 and s >= 65):
        return 0
    if step%2 == 0:
        return f(s + 1, step + 1) or f(s + 2, step + 1) or f(s*3, step + 1)
    return f(s + 1, step + 1) and f(s + 2, step + 1) and f(s*3, step + 1)


for s in range(1, 65):
    if f(s):
        print(s)
        break
