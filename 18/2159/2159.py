f = open('18/2159/2159.txt')

nums = [int(i) for i in f]

counter = 0

for i in range(len(nums)):
    for j in range(i + 9, len(nums)):
        counter += (nums[i] + nums[j])%2

print(counter)