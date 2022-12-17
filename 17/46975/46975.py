f = open('ege/17/46975/17.txt')


# nums = []
# for i in f:
#     nums.append(int(i))

nums = [int(i) for i in f]


# ОТДЕЛЬНО ищем ср арифм четных чисел
chetnie = []

for i in nums:
    if i%2 == 0: 
        chetnie.append(i)

avg = sum(chetnie)//len(chetnie)


counter = 0
max_summa = -1
# пара - два рядом стоящих элемента
for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if (nums[i]%3 == 0 and nums[j] < avg) or \
            (nums[j]%3 == 0 and nums[i] < avg):
            counter += 1
            max_summa = max(max_summa, nums[i] + nums[j])


print(counter, max_summa)