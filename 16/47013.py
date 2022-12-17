answ = []

# 0 1 1 2 

for i in range(10**9): # n = 10
    if i == 0:
        answ.append(0)
    elif i%2 == 1:
        answ.append(answ[-1] + 1)
    else:
        answ.append(answ[i//2])


print(answ.count(3))


# answ = []

# def f(n):
#     if n == 0: return 0
#     elif n%2: return f(n - 1) + 1
#     return f(n//2)

# for i in range(100):
#     answ.append(f(i))

# print(answ, answ.count(3))