import string

f = open('24/5677/24_5677.txt').readline()

for i in string.ascii_uppercase:
    if i not in 'AD':
        f = f.replace(i, ' ')


words = [i for i in f.split() if 'DAD' in i]

longest_word = ''

for i in words:
    if i.count('DAD') > longest_word.count('DAD'):
        longest_word = i


longest_word = longest_word.replace('DAD', '---')
print(longest_word)
# проверили что подходит глазами
print(len(longest_word))