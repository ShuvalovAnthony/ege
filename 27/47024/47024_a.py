f = open('27/47024/27-A.txt')

nums = []

for i in f:
    nums.append(int(i))


# [0, 1, 2, 3, 1111]


counter = 0

for i in range(len(nums)):
    summa = 0
    for j in range(i, len(nums)):
        summa += nums[j]
        if summa%1111 == 0:
            counter += 1

print(counter)

# способ 2
# counter = 0

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums) + 1):
#         if sum(nums[i:j])%1111 == 0:
#             counter += 1

# print(counter)