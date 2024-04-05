f = open("vars/dosrok2024/17/17.txt")

nums = [int(i) for i in f]


for num in sorted(nums):
    if num%100 == 15:
        minNa15 = num
        break


def check(n1, n2, n3):
    return (
        ((n1%100 == 15) or (n2%100 == 15) or(n3%100 == 15)) and
        (n1**2 + n2**2 + n3**2 >= minNa15)
    )


maxSum = 0
counter = 0

for i in range(len(nums) - 2):
    if check(nums[i], nums[i + 1], nums[i + 2]):
        maxSum = max(maxSum, nums[i] + nums[i + 1] + nums[i + 2])
        counter += 1

print(counter, maxSum)