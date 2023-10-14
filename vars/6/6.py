from itertools import *
from ipaddress import *
from collections import Counter

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

# 3 - 5398550

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

# 11 - 21

# 12 - 111

# s = '561'*102

# while '56' in s or '1111' in s:
#     s = s.replace('56', '1', 1)
#     s = s.replace('1111', '1', 1)

# print(s)

# 13 - 16
# counter = 0
# for addr in IPv4Network('184.178.54.144/255.255.255.240'):
#     bin_addr = bin(int(addr))[2:]
#     if '111' in bin_addr:
#         counter += 1

# print(counter)

# 14 - 4
# num = 9**9 + 3**21 - 7

# digits = []

# while num > 0:
#     digits.append(num%3)
#     num //= 3

# print(digits.count(0))

# 15 - 50

# def p(x): return 11 <= x <= 28

# def q(x): return 5 <= x <= 55

# def a(x, start, stop): return start < x < stop

# coords = combinations(sorted([11, 28, 5, 55]), 2)

# dlini = set()

# for start, stop in coords:
#     flag = True
#     for x in range(0, 100):
#         if (
#             a(x, start, stop) and (
#                 not ((not p(x)) <= q(x))
#             )
#         ):
#             flag = False
#             break

#     if flag:
#         dlini.add(stop - start)

# print(dlini, max(dlini))

# 16 - 27

# def f(n):
#     if n <= 15: return 2*n**2 + 4*n + 3
#     elif n%3 == 0: return f(n - 1) + n**2 + 3
#     return f(n - 2) + n - 6

# def check(n):
#     for i in str(n):
#         if int(i)%2 == 0: return False
#     return True

# counter = 0
# for n in range(1, 1001):
#     counter += check(f(n))

# print(counter)

# 17 - 4 13248

# nums = [int(i) for i in open('vars/6/17.txt')]

# max_krat_13 = 0

# for num in nums:
#     if num%13 == 0:
#         max_krat_13 = max(max_krat_13, num)

# counter = 0
# min_summ = 10**6

# for i in range(len(nums) - 1):
#     if nums[i]%max_krat_13 == 0 or nums[i + 1]%max_krat_13 == 0:
#         counter += 1
#         min_summ = min(min_summ, nums[i] + nums[i + 1])

# print(counter, min_summ)

# 18 - 456
# nums = [float(i) for i in open('vars/6/18.txt')]
# # nums = [3.3, 5.2, 5.9, 1.3, 1.7, 4.5] # test example
# max_sum = 0
# temp_sum = 0

# for i in range(len(nums) - 1):
#     if nums[i + 1] < nums[i]:
#         temp_sum += nums[i]
#     else:
#         max_sum = max(max_sum, temp_sum + nums[i])
#         temp_sum = 0

# print(int(max_sum))

# 23 - 6

# def f(start, stop):
#     if (start > stop) or (start == 13): return 0
#     elif start == stop: return 1
#     return f(start + 1, stop) + f(start*2, stop) + f(start*3, stop)

# print(f(3, 8)*f(8, 18))

# 24 - U1618
# s = open('vars/6/24.txt').read()

# answ = ''

# for i in range(len(s) - 1):
#     if s[i] == 'X' and s[i + 1] != 'X':
#         answ += s[i + 1]

# print(Counter(answ).most_common(1))