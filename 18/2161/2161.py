f = open('18/2161/2161.txt')

nums = [float(i) for i in f]

max_summa = -10**6

summa = nums[0]

for i in range(len(nums) - 1):
    if abs(nums[i + 1] - nums[i]) > 20:
        summa += nums[i + 1]
        max_summa = max(max_summa, summa)
    else:
        max_summa = max(max_summa, summa)
        summa = nums[i + 1]


print(max_summa)
    