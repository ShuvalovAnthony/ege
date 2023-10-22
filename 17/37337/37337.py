f = open('17/37337/17.txt')

nums = [int(i) for i in f]

def check(num1, num2):
    if (
        (num1%160 != num2%160) and
        (num1%7 == 0 or num2%7 == 0)
    ):
        return True
    else:
        return False

counter = 0
max_summa = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if check(nums[i], nums[j]):
            counter += 1
            if nums[i] + nums[j] > max_summa:
                max_summa = nums[i] + nums[j]

            # max_summa = max(max_summa, nums[i] + nums[j])

print(counter, max_summa)
