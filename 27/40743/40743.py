f = open('27/40743/27-A.txt')

n = int(f.readline())

nums = [int(i) for i in f]

max_sum = -10**15

# функция куда подаем срез и проверяем что в нем колво четных положительных
# элементов кратно 30
def check(podposled:list): 
    counter = 0
    for i in podposled:
        if i%2 == 0 and i > 0: counter += 1
    return counter%30 == 0


for i in range(len(nums)):
    for j in range(i + 1, len(nums)): # в два цикла перебираем все возможные срезы
        podposled = nums[i:j + 1] # наш срез от i до j включительно
        if check(podposled): # проверяем первое условие
            max_sum = max(max_sum, sum(podposled)) # обновляем макс сумму если сумма среза больше текущей макс суммы

print(max_sum)