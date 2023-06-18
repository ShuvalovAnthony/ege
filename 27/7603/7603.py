# Задание A
# f = open('27__/7603/27A_7603.txt')

# n = int(f.readline())
# k = int(f.readline())

# nums = [int(i) for i in f]

# maximum = -1

# for i in range(len(nums)):
#     for j in range(i + 25, len(nums)):
#         summa = nums[i] + nums[j]
#         maximum = max(maximum, summa)

# print(maximum)

# Задание B на шару)0)


f = open('27__/7603/27B_7603.txt')

n = int(f.readline())
k = int(f.readline())

nums = [int(i) for i in f]

summa = 0

tmp_max = max(nums)
print(nums.index(tmp_max))


summa += nums.pop(nums.index(tmp_max))
tmp_max = max(nums)
print(nums.index(tmp_max))
summa += nums.pop(nums.index(tmp_max))

print(summa)