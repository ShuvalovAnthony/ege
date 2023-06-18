f = open('9/9539/data.txt')


nums = [
    sorted([int(i) for i in stroka.split()]) # сортируем строки!!!!!
    for stroka in f
]

def check(stroka:list): # строку подаем отсортированную!!!!
    if (
        stroka[0] == stroka[1] and\
        stroka[-1] == stroka[-2] and
        stroka[0] < stroka[2] < stroka[-1] 
    ): return True

counter = 0

for stroka in nums:
    if check(stroka):
        print(stroka)
        counter += 1

print(counter)
