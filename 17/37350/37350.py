f = open('ege/17/37350/17.txt')

nums = [int(i) for i in f]

counter = 0
max_sum = -10**6

# 1000
for i in range(len(nums) - 1): # 0 - 998 i = 555
    for j in range(i + 1, len(nums)): # 556 557
        if (nums[i] + nums[j])%2 == 1 and\
            (nums[i]*nums[j])%3 == 0:
            counter += 1
            max_sum = max(max_sum, nums[i] + nums[j])


print(counter, max_sum)



# for i in range(10 - 1):
#     for j in range(i + 1, i + 2):
#         print(i ,j)