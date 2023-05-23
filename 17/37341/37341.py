f = open('17/37341/17.txt')

nums = [int(i) for i in f]


counter = 0
max_summa = 0


for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if (
            (nums[i] - nums[j])%2 == 0 and
            (nums[i]*nums[j])%19 == 0
        ):
            counter += 1
            max_summa = max(max_summa, nums[i] + nums[j])


print(counter, max_summa)
