f = open('27/35916/b.txt')

nums = sorted([int(i) for i in f])
# nums = [int(i) for i in f]

nums = nums[:100:]

result = 10**9


for i1 in range(len(nums)):
    for i2 in range(i1 + 1, len(nums)):
        for i3 in range(i2 + 1, len(nums)):
            res = nums[i1] + nums[i2] + nums[i3]
            if res%3 == 0:
                result = min(result, res)


print(result)



