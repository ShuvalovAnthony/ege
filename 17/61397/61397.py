f = open('17/61397/17.txt')

nums = [int(i) for i in f]



for num in sorted(nums, reverse=True):
    if str(num)[-2:] == '17':
        max_17 = num
        break


def check(num1, num2, num3):
    return (
        (
            sum(
                [(i in range(1000, 10000)) for i in (num1, num2, num3)]
                ) == 2
            ) and
        (
            any([(i%5 == 0) for i in (num1, num2, num3)])
        ) and
        (
            num1 + num2 + num3 > max_17
        )
    )


counter = 0
max_sum = 0

for i in range(len(nums) - 2):
    if check(nums[i], nums[i + 1], nums[i + 2]):
        counter += 1
        max_sum = max(max_sum, nums[i] + nums[i + 1] + nums[i + 2])


print(counter, max_sum)
