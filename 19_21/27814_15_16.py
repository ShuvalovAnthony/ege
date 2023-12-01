def f(s, step=1): # s - колво камней, step - шаг
    if s >= 70 and step == 3:
        return 1
    elif (step == 3 and s < 70) or (step < 3 and s >= 70):
        return 0
    return f(s + 1, step + 1) or f(s + 4, step + 1) or\
        f(s*5, step + 1)


print('задача 19')
for s in range(1, 70):
    if f(s):
        print(s)
        break

# ##########

# def f(s, step=1): # s - колво камней, step - шаг
#     if s >= 70 and step == 4:
#         return 1
#     elif (step == 4 and s < 70) or (step < 4 and s >= 70):
#         return 0
#     if step%2 == 1:
#         return f(s + 1, step + 1) or f(s + 4, step + 1) or f(s*5, step + 1)
#     return f(s + 1, step + 1) and f(s + 4, step + 1) and f(s*5, step + 1)

# print('задача 20')
# for s in range(1, 14):
#     if f(s):
#         print(s)

# ##########

def f(s, step=1): # s - колво камней, step - шаг
    if s >= 70 and step in (3, 5):
        return 1
    elif (step == 5 and s < 70) or (step < 5 and s >= 70):
        return 0
    if step%2 == 0:
        return f(s + 1, step + 1) or f(s + 4, step + 1) or f(s*5, step + 1)
    return f(s + 1, step + 1) and f(s + 4, step + 1) and f(s*5, step + 1)

print('задача 21')
for s in range(1, 14):
    if f(s):
        print(s)
        break


