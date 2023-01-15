# def f(n):
#     while (n%2 == 0) or (n%3 == 0):
#         if n%2 == 0:
#             n //= 2
#         if n%3 == 0:
#             n //= 3
#     if n == 1:
#         return True
#     return False


# for i in range(4*10**8, 6*10**8 + 1):
#     if f(i): print(i)
    
nums = []

for st2 in range(0, 31, 2):
    for st3 in range(1, 31, 2):
        nums.append((2**st2)*(3**st3))


# print(nums)

for num in nums:
    if 400000000 <= num <= 600000000:
        print(num)