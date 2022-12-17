f = open('ege/27__/35485/b.txt')

nums = sorted([int(i) for i in f], reverse=True)
# nums = [int(i) for i in f]

nums = nums[:100:]

result = 0


for i1 in range(len(nums)):
    for i2 in range(i1 + 1, len(nums)):
        for i3 in range(i2 + 1, len(nums)):
            res = nums[i1] + nums[i2] + nums[i3]
            if res%100003 == 0:
                result = max(result, res)


print(result)



