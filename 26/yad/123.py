f = open("26/yad/26.txt")


n = int(f.readline())

nums = sorted([int(i) for i in f])


maxSet = []


for start in range(len(nums)):
    tempSet = []
    lastStar = 1
    for i in range(start, len(nums)):
        if nums[i] >= lastStar*1.1:
            tempSet.append(nums[i])
            lastStar = nums[i]

    if len(tempSet) > len(maxSet):
        maxSet = tempSet
    elif (len(tempSet) == len(maxSet)) and (tempSet[-1] < maxSet[-1]):
        maxSet = tempSet

print(len(maxSet), maxSet[-1])