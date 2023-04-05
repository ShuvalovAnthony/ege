nums = []

for m in range(0, 31, 2): # m четное!!!!
    for n in range(1, 31, 2): # n - нечетное!!!
        nums.append((2**m)*(3**n))


# print(nums)

ordered_nums = []

for num in nums:
    if 2*10**8 <= num <= 4*10**8:
        ordered_nums.append(num)

print(sorted(ordered_nums))