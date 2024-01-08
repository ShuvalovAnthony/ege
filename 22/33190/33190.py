f = open('22/33190/33190.txt')

nums = [float(i) for i in f]


def maxSubListSum(subList):
    max_sum = 0
    for i in range(len(subList) - 1):
        for j in range(i + 1, len(subList) + 1):
            max_sum = max(
                max_sum,
                sum(subList[i:j])
            )
    return max_sum


def validSubList(subList):
    for i in range(1, len(subList)):
        if abs(subList[i] - subList[i - 1]) > 10: return False
    return True



max_summa = -10**6

for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        subList = nums[i: j]
        if validSubList(subList):
            max_summa = max(
                max_summa,
                maxSubListSum(subList)
            )

print(int(max_summa))

