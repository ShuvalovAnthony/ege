f = open('17/6360/17_6360.txt')


nums = [int(i) for i in f]

min_num_end_with_7 = -1

for i in sorted(nums):
    if str(i)[-1] == '7':
        min_num_end_with_7 = i
        break

kv_min_num_ends_with_7 = min_num_end_with_7**2

counter = 0
max_summa_kv = -1

def check(num1, num2):
    if (
        (str(num1)[-1] == str(num2)[-1]) and\
        ((num1%7 == 0) and (num2%7 != 0) or\
         (num1%7 != 0) and (num2%7 == 0)
        ) and\
        ((num1**2 + num2**2) <= kv_min_num_ends_with_7)
    ): return (num1**2 + num2**2)
    return False


for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if check(nums[i], nums[j]):
            counter += 1
            max_summa_kv = max(max_summa_kv, check(nums[i], nums[j]))

print(counter, max_summa_kv)

