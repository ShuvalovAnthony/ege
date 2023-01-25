from string import ascii_uppercase

f = open('24/35482/24.txt')

strings = [i.strip() for i in f] # сохраняем все строчки в список строк

min_g = 10**6 # колво букв G по умолчания - миллион

string_with_less_g = '' # здесь мы храним строчку, в которой после пробега по всему файлу,
                        # будет меньше всего букв G


for string in strings: # бежим по всем строчкам в файле
    if string.count('G') < min_g: # если количество G СТРОГО меньше, чем минимальное предыдущее
        min_g = string.count('G') # тогда обновляем минимальное количество букв G
        string_with_less_g = string # и соотв обновляем строку с минимальным количеством G

res_letter = '' # ОТВЕТ

max_count = 0
res_letter = ''
for letter in ascii_uppercase: # бежим по всем заглавным буквам англ алфавита
    if string_with_less_g.count(letter) >= max_count:
        max_count = string_with_less_g.count(letter)
        res_letter = letter


print(res_letter)