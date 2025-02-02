from string import punctuation

f = open("ege/10/72595/text.txt").read().lower()


for i in punctuation:
    f = f.replace(i, ' ')


count = 0

for word in f.split():
    if (word[0] == "я") and (word[-1] == 'а'):
        count += 1

print(count)