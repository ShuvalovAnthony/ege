f = open('17_n/5882/17_5882.txt')


nums = [int(i) for i in f]


nums_end_with_3 = []


for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if (
            ((str(nums[i])[-1] == '3') and (str(nums[j])[-1] != '3')) or\
            ((str(nums[i])[-1] != '3') and (str(nums[j])[-1] == '3'))
        ):
            nums_end_with_3 += [nums[i], nums[j]]


min_elem = min(nums_end_with_3)
summa_kv_cifr = sum([int(i)**2 for i in str(abs(min_elem))])

def check(num):
    if (
        ('3' in str(num)) and\
        (num > summa_kv_cifr)
    ): return True
    return False

counter = 0
min_num = 10**6

for num in nums:
    if check(num):
        counter += 1
        min_num = min(min_num, num)

print(counter, min_num)
