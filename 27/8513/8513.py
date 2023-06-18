f = open('27__/8513/27_B_8513.txt')

k = int(f.readline())
n = int(f.readline())

nums = [int(i) for i in f]

max_1 = [-1, -1]
max_2 = [-1, -1]
max_3 = [-1, -1]
max_4 = [-1, -1]
max_5 = [-1, -1]
max_6 = [-1, -1]
print(k)

for i in range(len(nums)):
    if nums[i] > max_1[0]:
        max_1 = [nums[i], i]
    elif nums[i] > max_2[0]:
        max_2 = [nums[i], i]
    elif nums[i] > max_3[0]:
        max_3 = [nums[i], i]
    elif nums[i] > max_4[0]:
        max_4 = [nums[i], i]
    elif nums[i] > max_5[0]:
        max_5 = [nums[i], i]
    elif nums[i] > max_6[0]:
        max_6 = [nums[i], i]
# max_summa = -1

# for i in range(len(nums)):
#     for j in range(i + 1 + k, len(nums)):
#         max_summa = max(max_summa, nums[i] + nums[j])


# print(max_summa)

print(max_1, max_2, max_3, max_4, max_5, max_6)

print(1045460*2)