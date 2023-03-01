# Способ 1 через список 
l = []

def f(n, step=0):
    l.append(n)
    if step == 3: return 0
    return f(n + 1, step + 1) + f(n + 2, step + 1) + f(n*3, step + 1)



f(4)

counter = 0
for i in l:
    if i%2 == 0: counter += 1

print(counter)


# Способ 2 через глоабульную переменную 
counter = 0

def f(n, step=0):
    global counter
    if n%2 == 0: counter += 1
    if step == 3: return 0
    return f(n + 1, step + 1) + f(n + 2, step + 1) + f(n*3, step + 1)

f(4) # НЕ ЗАБЫТЬ ВЫЗВАТЬ ФУНКЦИЮ!

print(counter)