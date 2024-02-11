f = open("17/37347/17.txt")

nums = [int(i) for i in f]

counter = 0
max_sum = 0


for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        left = nums[i]
        right = nums[j]

        if (
            left*right%14 != 0
        ):
            counter += 1
            max_sum = max(max_sum, left + right)


print(counter, max_sum)