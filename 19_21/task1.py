def f(s, step=1): # s - колво камней, step - шаг
    if s >= 88 and step == 3:
        return 1
    elif (step == 3 and s < 88) or (step < 3 and s >= 88):
        return 0
    return f(s + 1, step + 1) or f(s*3, step + 1)

print('задача 19')
for s in range(1, 88):
    if f(s):
        print(s)
        break


def f(s, step=1): # s - колво камней, step - шаг
    if s >= 88 and step == 4:
        return 1
    elif (step == 4 and s < 88) or (step != 4 and s >= 88):
        return 0
    if step%2:
        return f(s + 1, step + 1) or f(s*3, step + 1)
    return f(s + 1, step + 1) and f(s*3, step + 1)

print('задача 20')
for s in range(1, 88):
    if f(s):
        print(s)


def f(s, step=1): # s - колво камней, step - шаг
    if s >= 88 and step == 3:
        return 1
    elif (step == 3 and s < 88) or (step < 3 and s >= 88):
        return 0
    if not step%2:
        return f(s + 1, step + 1) or f(s*3, step + 1)
    return f(s + 1, step + 1) and f(s*3, step + 1)

print('задача 21')
for s in range(1, 88):
    if f(s):
        print(s)
        break