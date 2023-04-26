f = open('9/47213/47213.txt')

nums = [list(map(int, i.split())) for i in f]


def check(nums):
    if len(nums) != len(set(nums)) + 1: return False

    povtor = None
    summa_nepovtor = 0
    for num in nums:
        if nums.count(num) == 2: povtor = num
        else: summa_nepovtor += num
    return summa_nepovtor/4 <= povtor*2

counter = 0

for stroka in nums:
    counter += check(stroka)

print(counter)


# Второй вариант, попроще для понимания

def check(nums):
    if len(nums) != len(set(nums)) + 1: return False

    povtor = []
    nepovtor = []
    for num in nums:
        if nums.count(num) == 2: povtor.append(num)
        else: nepovtor.append(nums)

    return sum(nepovtor)/4 <= sum(povtor)
    