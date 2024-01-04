f = open('9/58323/58323.txt')

nums = []

for row in f:
    nums += [float(i) for i in row.split()]


nums = sorted(nums)

print(nums[:10])
print(nums[-10:])

print(len(nums) - 4)