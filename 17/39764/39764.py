f = open('17/39764/17.txt')

nums = [int(i) for i in f]



def check(a, b, c):
    sides = sorted([a, b, c])
    return sides[2]**2 == sides[0]**2 + sides[1]**2



counter = 0
max_summa = 0

for i in range(len(nums) - 2):
    if check(nums[i], nums[i + 1], nums[i + 2]):
        counter += 1
        max_summa = max(
            max_summa,
            nums[i] + nums[i + 1] + nums[i + 2]
        )


print(counter, max_summa)

