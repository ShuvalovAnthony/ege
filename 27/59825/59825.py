f = open("27/59825/27-A.txt")

k = int(f.readline())
n = int(f.readline())


nums = []

for i in range(n):
    nums.append([int(f.readline()), i])

nums = sorted(nums, reverse=True)


newList = nums[:50]


def maxdistance(a,b,c):
    return max(abs(a[-1] - b[-1]), abs(a[-1] - c[-1]), abs(b[-1] - c[-1]))

max_sum = 0

for i in range(len(newList)):
    for j in range(i + 1, len(newList)):
        for k in range(j + 1, len(newList)):
            if maxdistance(newList[i], newList[j], newList[k]):
                max_sum = max(max_sum, newList[i][0] + newList[j][0] + newList[k][0])

print(max_sum)