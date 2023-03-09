f = open('17/39763/17.txt')

nums = []

for i in f: nums.append(int(i))


count = 0
max_summa = 0

for i in range(len(nums) - 2):
    if ((nums[i]**2 + nums[i + 1]**2 == nums[i + 2]**2) and
    (nums[i + 1]**2 + nums[i + 2]**2 == nums[i]**2) and
    (nums[i + 2]**2 + nums[i]**2 == nums[i + 1]**2)):
        count += 1
        max_summa = max(max_summa, sum([nums[i], nums[i + 1], nums[i + 2]]))

print(count, max_summa)