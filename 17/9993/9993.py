f = open('17/9993/17_9993.txt')


nums = [int(i) for i in f]

for num in sorted(nums, reverse=True):
    if str(num)[-2:] == '17':
        max_17 = num
        break


def prime(num):
    if num < 0: return False
    for i in range(2, int(num**0.5)):
        if num%i == 0: return False
    return True


counter = 0
max_mult = -10**9

for i in range(len(nums) - 1):

    if (
        (
            (nums[i] + nums[i + 1])%max_17 == 0
        ) and
        (
            (prime(nums[i]) + prime(nums[i + 1])) == 1
        )
    ):
        counter += 1
        max_mult = max(
            max_mult,
            nums[i]*nums[i + 1]
        )

print(counter, max_mult)