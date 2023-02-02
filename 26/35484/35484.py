f = open('26/35484/35484.txt')

all_nums = []
chet_nums = []

for i in f:
    num = int(i)
    all_nums.append(num)
    if num%2 == 0: chet_nums.append(num)

#  по условию все числа различны - можем сделать set()
all_nums = set(all_nums) # преобразование в сет кратно ускоряет поиск


max_avg = 0
counter_avg = 0

for i in range(len(chet_nums) - 1):
    for j in range(i + 1, len(chet_nums)):
        avg = (chet_nums[i] + chet_nums[j])//2
        if avg in all_nums:
            counter_avg += 1
            max_avg = max(max_avg, avg)


print(counter_avg, max_avg)