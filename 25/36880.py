nums = []

for st2 in range(0, 31, 2):
    for st3 in range(1, 31, 2):
        nums.append((2**st2)*(3**st3))


# print(nums)

for num in nums:
    if 400000000 <= num <= 600000000:
        print(num)