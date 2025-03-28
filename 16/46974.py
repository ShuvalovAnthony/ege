from datetime import datetime

# start_time = datetime.now()

# nums = []

# # 0 1 1 2 

# for i in range(10**9): # n = 10
#     if i == 0:
#         nums.append(0)
#     elif i%2 == 1:
#         nums.append(nums[-1] + 1)
#     else:
#         nums.append(nums[i//2])

#     if i%10**6 == 0:
#         print(i)


# print(nums.count(2))
# print(datetime.now() - start_time)


# answ = []

# def f(n):
#     if n == 0: return 0
#     elif n%2: return f(n - 1) + 1
#     return f(n//2)

# for i in range(100):
#     answ.append(f(i))

# print(answ, answ.count(3))

from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    if n%2: return f(n - 1) + 1
    return f(n//2)


counter = 0

for n in range(10**9):
    counter += f(n) == 2
    
    if n%10**6 == 0:
        print(n)


print(counter)