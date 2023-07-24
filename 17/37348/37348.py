f = open("17/37348/17.txt")
nums = [int(i) for i in f]

count = 0
maxsum = -1

for i in range (len(nums)-1):
    for j in range (i + 1, len(nums)):
        if ((nums[i]*nums[j])%34):
            count += 1
            maxsum = max(maxsum, (nums[i]+nums[j]))

print(count, maxsum)