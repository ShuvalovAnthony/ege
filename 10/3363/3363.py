from string import punctuation

f = open("10/3363/10_3363.txt").read()

for i in punctuation:
    f = f.replace(i, '')

counter = 0

words = []

for word in f.split():
    if word == 'что': 
        words.append(word)

print(set(words))