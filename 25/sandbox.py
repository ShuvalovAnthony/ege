nums = []

for m in range(2, 31, 2):
    for n in range(1, 31, 2):
        nums.append((2**m)*(3**n))

for num in sorted(nums):
    if 200_000_000 <= num <= 400_000_000: print(num)