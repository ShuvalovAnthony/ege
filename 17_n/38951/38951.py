f = open('ege/17/38951/17.txt')

nums = [int(i) for i in f]

counter = 0
max_summa = -1

for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if ((nums[i]*nums[j])%3 == 0) and \
            ((nums[i] + nums[j])%5 == 0):
            counter += 1
            max_summa = max(max_summa, nums[i] + nums[j])


print(counter, max_summa)