f = open('10/7589/7589.txt').read()

for i in ".,:;/?!\'\"()":
    f = f.replace(i, '')

f = f.split()

counter = 0

for i in f:
    if ('час' in i.lower()) and (len(i) > 3): counter += 1

print(counter)