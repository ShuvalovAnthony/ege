f = open('17/48438/17.txt')


nums = [int(i) for i in f]


for num in sorted(nums):
    if str(num)[-1] == '7':
        min_na_7 = num
        break

kv_min_na_7 = min_na_7**2

counter = 0
max_summa = -1

def check7(num1, num2):
    if (abs(num1)%10 == 7 and abs(num2)%10 != 7) or\
        (abs(num2)%10 == 7 and abs(num1)%10 != 7):
        return True
    return False

for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if check7(nums[i], nums[j]) and\
            (nums[i]**2 + nums[j]**2 < kv_min_na_7):
            counter += 1
            max_summa = max(max_summa, nums[i]**2 + nums[j]**2)

print(counter, max_summa)
