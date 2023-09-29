f = open('17/39763/17.txt')

nums = []

for i in f: nums.append(int(i))


count = 0
max_summa = 0

for i in range(len(nums) - 2):
    sides = sorted([nums[i], nums[i + 1], nums[i + 2]])
    if (sides[-1]**2 < sides[0]**2 + sides[1]**2):
        count += 1
        max_summa = max(max_summa, sum([nums[i], nums[i + 1], nums[i + 2]]))

print(count, max_summa)