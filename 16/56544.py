def f(a, b):
    if b == 0: return 0
    elif a > b: return f(a - 1, b) + b
    return f(a, b - 1) + a


deliteli = set()

# for a in range(10):
#     for b in range(10):
#         print("a=", a, "b=", b, f(a, b))

# Укажите количество таких целых неотрицательных чисел a, для которых можно подобрать такое b, что F(a, b)  =  2 097 152.

for i in range(1, int(2097152**0.5) + 1):
    if 2097152%i == 0:
        deliteli.add(i)
        deliteli.add(2097152//i)


print(len(deliteli))
