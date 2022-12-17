f = open('ege/18__/data.txt')

nums = []

for i in f:
    num = float(i.replace(',', '.'))
    nums.append(num)


max_summa = -10**6


summa = nums[0]

for i in range(len(nums) - 1):
    if nums[i + 1] < nums[i]:
        summa += nums[i + 1]
    else:
        max_summa = max(max_summa, summa)
        summa = nums[i + 1]


print(max_summa)
    

