res = [4]

counter = 1

for step_number in range(3): # step_number - количество повторений
    tmp_res = [] # промежуточный список в котором хранится каждое преобразованное число из предыдущего списка  
    for i in res: # всеми возможными операциями (командами)
        tmp_res += [i + 1, i + 2, i*3]
    res = tmp_res.copy() # перезаписываю список начальный, чтобы можно было зациклить задачу
    for i in res:
        if i%2 == 0: counter += 1

print(counter)