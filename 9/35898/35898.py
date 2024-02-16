f = open("9/35898/35898.txt")

nums = []

for row in f:
    nums += [float(i) for i in row.split()]


counter = 0

for i in range(len(nums) - 1):
    if nums[i] - nums[i + 1] >= 2:
        counter += 1

print(counter)

