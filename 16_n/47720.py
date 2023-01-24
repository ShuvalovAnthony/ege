import sys

sys.setrecursionlimit(15000)


def f(n):
    if n == 1:
        return 1
    return f(n - 1)*n

a = f(2023)
b = f(2020)

print(a//b)


# answ = ['ABOBUS']

# for i in range(1, 2025):
#     if i == 1: answ.append(1)
#     else: answ.append(answ[-1]*i)



# print(answ[2023]//answ[2020])





