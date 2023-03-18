f = open('26/2653.py/26_2653.txt')

n = int(f.readline())

pos_sum = set() # возможные суммы

weights = [int(i) for i in f]

for weight in weights:
    [pos_sum.add(summa + weight) for summa in pos_sum.copy()]
    pos_sum.add(weight)

max_impossible_summ = 0

for i in range(sum(weights), 0, -1): # идем от самого большого числа
    if i not in pos_sum:            # если такого числа нет в
        max_impossible_summ = i     # списке возможных
        break                       # сохраняем его и оставнавливаемся

# sum(weights) - (len(pos_sum)) - количество весов, которые
# нельзя набрать (максимальный вес как сумма всех гирь минус
#                 количество возможных наборов весов)

print(sum(weights) - (len(pos_sum)), max_impossible_summ)