from itertools import *


# 1 - 20

# 2 - yzwx
# def f(x, y, z, w):
#     return (
#         ((z <= y) and ((not x) <= w)) <= 
#         ((z == w) or (y and (not x)))
#     )

# for a in product([0, 1], repeat=5):
#     t = [(0, 0, a[0], 0), (0, a[1], a[2], a[3]), (1, a[4], 1, 1)]
#     if len(t) == len(set(t)):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
#                 for r in t:
#                     print(''.join(p))

# 3 - 30415

# 4 - 12

# 5 - 16
# for n in range(1000, 2, -1):
#     n_bin = bin(n)[2:]
#     if n%4 == 0:
#         n_bin += n_bin[-2:]
#     else:
#         n_bin = bin(2*(n%4))[2:] + n_bin

#     r = int(n_bin, 2)
#     if r < 68:
#         print(n)
#         break

# 7 - 2

# 8 ??

# 9 - 86
# f = open('vars/6/9.txt')

# def check(stroka: str):
#     nums = [int(i) for i in stroka.split()]
#     if len(set(nums)) != len(nums): return False
#     chet_counter = 0
#     chet_summ = 0
#     nechet_summ = 0
#     for num in nums:
#         if num%2 == 0:
#             chet_counter += 1
#             chet_summ += num
#         else:
#             nechet_summ += num
#     return (chet_counter < 3) and (chet_summ > nechet_summ)


# counter = 0

# for i in f.readlines():
#     counter += check(i)

# print(counter)

# 10 - 10

# 11 - 