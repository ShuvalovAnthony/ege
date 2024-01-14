f = open("27/28133/28133_B.txt")

n = f.readline()

nums = [int(i) for i in f]


res = []


for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        summa = nums[i] + nums[j]
        if (
            nums[i] > nums[j] and
            summa%120 == 0
            ):
            res.append([summa, nums[i], nums[j]])


if res: print(max(res))
else: print('00')