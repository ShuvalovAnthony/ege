f = open('ege/17/37336/17.txt')


nums = []

for i in f: nums.append(int(i))


count = 0
max_summa = -10**6

for i in range(len(nums) - 1):
    if nums[i]*nums[i + 1]%3 == 0:
        count += 1
        max_summa = max(nums[i] + nums[i + 1], max_summa)

print(count, max_summa)