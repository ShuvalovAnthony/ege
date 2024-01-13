f = open('27/27989/27989_B.txt')

nums = [int(i) for i in f]

counter = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        res = nums[i]*nums[j]
        if res%26 == 0: counter += 1

print(counter)