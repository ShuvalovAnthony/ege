alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

word = "РЕКУРСИЯ"[::-1]
number = 1


for i in range(len(word)):
    number += alph.index(word[i])*33**i

print(number)