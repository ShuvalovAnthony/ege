f = open('ege/26/27423/26_demo.txt')


s, n = map(int, f.readline().split()) # s - свободное место под архивы
                                    # - колво пользователей

users_data = [] # список со всеми архивами

for i in f: # заполняем список всхе данных (из текстового файла)
    users_data.append(int(i))

users_data = sorted(users_data) # сортируем по возрастанию

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
print(saved)
print('-----')
print(users_data)



   