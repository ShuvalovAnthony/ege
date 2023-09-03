from string import punctuation

f = open('10/6761/6761.txt').read()

# удаляем все знаки препинания
for i in punctuation:
    f = f.replace(i, '')

counter = 0

for word in f.lower().split(): # f.lower() - все маленькими (чтобы игнорировать регистр) .split() - список слов
    if word in ('как', 'что'): # word == 'как' or word == 'что'
        counter += 1

print(counter)