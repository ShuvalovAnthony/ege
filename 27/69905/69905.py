f = open("ege/27/69905/2772.txt")

nums = [int(i) for i in f]


mini = min(nums)

min_indexes = [i for i in range(len(nums)) if nums[i] == mini]

max_sum = 0

for j in min_indexes:
    si = max(nums[:j])
    ki = max(nums[j + 1:])

    max_sum = max(max_sum, si + ki - 2*mini)


print(max_sum)