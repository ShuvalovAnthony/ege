# def f(s, step=1): # p - 1 v - 2 p - 3
#     if step == 3 and s >= 70: return 1
#     elif (step < 3 and s >= 70) or (step == 3 and s < 70): return 0
#     return f(s + 1, step + 1) or f(s + 4, step + 1) or f(s*5, step + 1)


# print('задача 19')
# for s in range(1, 70): # 1 <= s <= 69
#     if f(s):
#         print(s)
#         break





# def f(s, step=1): # p - 1    v - 2    p - 3 !!!! v - 4
#     if step == 4 and s >= 70: return 1
#     elif (step < 4 and s >= 70) or (step == 4 and s < 70): return 0
#     if step%2 == 1: # 1 3 5
#         return f(s + 1, step + 1) or f(s + 4, step + 1) or f(s*5, step + 1)
#     return f(s + 1, step + 1) and f(s + 4, step + 1) and f(s*5, step + 1)

# print('задача 20')
# for s in range(1, 70): # 1 <= s <= 69
#     if f(s):
#         print(s)
        


# def f(s, step=1): # p - 1    v - 2    p - 3 !!!! v - 4
#     if (step in (3, 5)) and s >= 70: return 1
#     elif (step < 5 and s >= 70) or (step == 5 and s < 70): return 0
#     if step%2 == 1: # 1 3 5
#         return f(s + 1, step + 1) and f(s + 4, step + 1) and f(s*5, step + 1)
#     return f(s + 1, step + 1) or f(s + 4, step + 1) or f(s*5, step + 1)

# print('задача 21')
# for s in range(1, 70): # 1 <= s <= 69
#     if f(s):
#         print(s)
#         break


def f(n):
    if n == 10**100: return 1
    print(n)
    return f(n + 1)


print(f(1))