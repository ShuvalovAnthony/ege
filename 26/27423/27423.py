f = open('26/27423/26_demo.txt')


s, n = map(int, f.readline().split()) # s - свободное место под архивы
                                    # - колво пользователей

users_data = sorted([int(i) for i in f]) # список со всеми архивами

saved = [] # - список сохранненых архивов (ЕГО ДЛИНА - КОЛВО СОХР АРХИВОВ)
# макс элемент - будет последним тк заполняем по возрастанию

for i in range(len(users_data)): # бежим по всем архивам

    if s < users_data[i]: # если нет свободного места под текущий архив - остановка цикла
        break

    s -= users_data[i] # если сюда дошли, значит место есть... 
    saved.append(users_data[i]) #  - добавляем в сохраненные архивы

# users_data = users_data[len(saved)::] # оставляем несохраненные файлы

print('свободное место', s)

print(len(saved), saved[-1])
print('-----')
print(users_data[-10::])




   