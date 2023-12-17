alph = sorted('ВЕРОНИКА')

words = []

for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            word = a1 + a2 + a3
            if word.count('В') == 1:
                words.append(word)



for word in words:
    if word.count('А') == 0:
        print(words.index(word) + 1)
        break