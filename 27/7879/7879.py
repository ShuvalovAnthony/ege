f = open('27__/7879/27A_7879.txt')

n = int(f.readline())
k = int(f.readline())

nums = [int(i) for i in f]

max_summa = -1

for i in range(len(nums)):
    for j in range(i + 1 + k, len(nums)):
        if ((nums[i] + nums[j])%2023 == 0) and\
        (
            ((nums[i]%47 == 0) and (nums[j]%47 != 0)) or\
            ((nums[j]%47 == 0) and (nums[i]%47 != 0))
        ):
            max_summa = max(
                max_summa,
                nums[i] + nums[j]
            )


print(max_summa)