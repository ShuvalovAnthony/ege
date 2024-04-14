f = open("27/27990/27990_A.txt")

n = f.readline()


nums = [int(i) for i in f]

counter = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i]*nums[j]%62 == 0:
            counter += 1

print(counter)