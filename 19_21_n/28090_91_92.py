def f(s, step=1):
    if step == 3 and s >= 46: return 1
    elif (step < 3 and s >= 46) or (step == 3 and s < 46):
        return 0
    return f(s + 1, step + 1) or f(s*2, step + 1)

print('задача 19')
for s in range(1, 46):
    if f(s):
        print(s)
        break




def f(s, step=1):
    if step == 4 and s >= 46: return 1
    elif (step < 4 and s >= 46) or (step == 4 and s < 46):
        return 0
    if step%2:
        return f(s + 1, step + 1) or f(s*2, step + 1)
    return f(s + 1, step + 1) and f(s*2, step + 1)

print('задача 20')
for s in range(1, 46):
    if f(s):
        print(s)
        