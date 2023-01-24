f = open('ege/17/37354/123.txt')

nums = [int(i) for i in f]

counter = 0
max_sum = -10**6


for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j])%2 == 1 and\
            (nums[i]*nums[j])%5 == 0:
            counter += 1
            max_sum = max(max_sum, nums[i] + nums[j])


print(counter, max_sum)