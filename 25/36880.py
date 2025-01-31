nums = []

for m in range(0, 31, 2):
    for n in range(1, 31, 2):
        nums.append((2**m)*(3**n))


# print(nums)

for num in nums:
    if 400000000 <= num <= 600000000:
        print(num)