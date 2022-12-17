f = open('ege/17/47221/17.txt')


nums = [] # все числа
max_el_sq = 0 # квадрат максимального элемента

for i in f:
    num = int(i) # строку переводим в число
    nums.append(num) # в список чисел добавляем ВСЕ числа
    if num%10 == 3: # если последняя цифра - 3
        max_el_sq = max(max_el_sq, num**2) # обновляем
        # квадрат максимального числа оканчивающегося на 3
    
counter = 0
max_summa = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, i + 2):
        if ((str(nums[i])[-1] == '3' and str(nums[j])[-1] != '3') or \
            (str(nums[i])[-1] != '3' and str(nums[j])[-1] == '3')) and \
            ((nums[i]**2 + nums[j]**2) >= max_el_sq):
            counter += 1
            max_summa = max(max_summa, (nums[i]**2 + nums[j]**2))

print(counter, max_summa)