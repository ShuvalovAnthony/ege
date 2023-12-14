f = open('17/55604/17.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    num = str(num)
    if num[-1] == num[-2]:
        kv_naim = int(num)**2
        break


counter = 0
max_summa_kvadratov = -1


def check(num1, num2):
    if (
        (
            (str(num1)[-1] == str(num2)[-2]) or
            (str(num2)[-1] == str(num1)[-2])
        ) and
        (
            (num1%7 == 0 and num2%7 != 0) or
            (num2%7 == 0 and num1%7 != 0)
        ) and
        (
            num1**2 + num2**2 <= kv_naim
        )
    ): return True

    return False


for i in range(len(nums) - 1):
    if check(nums[i], nums[i + 1]):
        counter += 1
        max_summa_kvadratov = max(
            max_summa_kvadratov,
            nums[i]**2 + nums[i + 1]**2
        )


print(counter, max_summa_kvadratov)