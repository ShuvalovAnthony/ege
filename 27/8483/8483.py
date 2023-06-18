f = open('27__/8483/27a_8483.txt')

n = int(f.readline())
delta = int(f.readline())

nums = [int(i) for i in f]

max_summa = 0

for i in range(len(nums)):
    for j in range(i + 1 + delta, len(nums)):
        for k in range(j + 1 + delta, len(nums)):
            max_summa = max(
                max_summa,
                nums[i] + nums[j] + nums[k]
            )

print(max_summa)