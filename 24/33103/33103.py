f = open('ege/24/33103/inf_22_10_20_24.txt')

counter = 0

for i in f:
    if i.count('A') > i.count('E'): counter += 1

print(counter)