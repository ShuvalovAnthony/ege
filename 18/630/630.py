f = open("18/630/630.txt")

nums = [float(i.replace(',', '.')) for i in f]



max_summa = -1
temp_summa = 0


for i in range(len(nums) - 1):
    if nums[i + 1] > nums[i]:
        temp_summa += nums[i]
    else:
        temp_summa += nums[i]
        max_summa = max(max_summa, temp_summa)
        temp_summa = 0

temp_summa += nums[-1]
max_summa = max(max_summa, temp_summa)


print(int(max_summa))