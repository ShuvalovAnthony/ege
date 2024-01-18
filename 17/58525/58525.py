f = open('17/58525/17.txt')

nums = [int(i) for i in f]

for num in sorted(nums, reverse=True):
    if (abs(num) in range (100, 1000))and (abs(num)%10 == 3):
        naim = num

def f(num1, num2):
    if (
        (
            ((num1 in range (1000, 10000)) + \
            (num2 in range (1000, 10000))) == 1
        ) and
        (
            (num1 ** 2 + num2 ** 2)%naim == 0
        )
    ): return True
    return False 

kolichestvo = 0
max_sumkv = 0

for i in range(len(nums) - 1):
    for j in range (i + 1, i + 2):
        if f(nums[i], nums[j]):
            kolichestvo += 1

            max_sumkv = max(max_sumkv, nums[i] ** 2 + nums[j] ** 2)

print(kolichestvo, max_sumkv)