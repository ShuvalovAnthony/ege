from string import punctuation

f = open('10/6761/6761.txt').read()

counter = 0

for i in punctuation:
    f = f.replace(i, '')

for word in f.lower().split():
    if word in ('как', 'что'):
        counter += 1

print(counter)