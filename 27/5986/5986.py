f = open('27__/5986/27B.txt')

nums = []
for i in f:
    if int(i)%2: nums.append(1) # 1 - нечетное
    else: nums.append(-1) # -1 - четное


max_len = 0

for j in range(len(nums) - 1):
    indexes_with_zero_sum = []

    summa = 0
    for i in range(j, len(nums)):
        summa += nums[i]
        if summa == 0:
            indexes_with_zero_sum.append(i)

    if len(indexes_with_zero_sum) >= 2:
        max_len = max(max_len, indexes_with_zero_sum[-1] - indexes_with_zero_sum[0])

print(max_len)
summa = 0