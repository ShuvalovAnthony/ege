f = open('9/59834/59834.txt')

nums = [list(map(int, i.split())) for i in f]


def check(nums):
    if len(set(nums)) != 5: return False

    summa_povtor = 0
    summa_nepovtor = 0
    for num in nums:
        if nums.count(num) == 2: summa_povtor += num
        else: summa_nepovtor += num
    return summa_povtor < summa_nepovtor/4

counter = 0

for stroka in nums: counter += check(stroka)

print(counter)
