f = open("27/9848/27_A_9848.txt")

k = int(f.readline())

nums = [int(i) for i in f]

maxSum = 0

for i in range(len(nums)):
    for j in range(i + k + 1, len(nums)):
        maxSum = max(
            maxSum,
            sum(nums[i:j])
        )


print(maxSum)