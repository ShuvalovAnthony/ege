f = open('17/45251/107_17.txt')


nums = [int(i) for i in f]


min_el = 10**6

for i in nums:
    if i%21 == 0 and i < min_el: min_el = i

counter = 0
max_sum = -10**6



for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if (nums[i]*nums[j])%min_el == 0:
            counter += 1
            max_sum = max(max_sum, nums[i] + nums[j])

print(counter, max_sum)