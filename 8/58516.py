from itertools import permutations


alph = 'ВИКОРТ'
index = 1


for word in permutations(alph, r=6):
    word = ''.join(word)

    if word == 'РОКВИТ':
        print(index, word, 'РОКВИТ')

    index += 1