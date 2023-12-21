f = open ('17/59842/1777.txt')

nums = [int(i) for i in f]

for num in sorted(nums, reverse=1):
    if str(num)[-2:] == '29':
        max_el = num
        break


def f(num1, num2, num3):
    if (
        (
            ((abs(num1) in range(10000, 100000)) +\
            (abs(num2) in range(10000, 100000)) +\
            (abs(num3) in range(10000, 100000))) == 2
        ) and
        (
            (num1 + num2 + num3) <= max_el
        )
    ): return True
    return False


kolichestvo = 0
max_summ = -1


for i in range (len(nums) -2):
    if f(nums[i], nums[i + 1], nums[ i + 2]):
        kolichestvo += 1
        max_summ = max(max_summ, nums[i] + nums[i + 1] + nums[i + 2])

print(kolichestvo, max_summ)