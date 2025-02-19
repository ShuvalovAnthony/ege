from collections import Counter

f = open("ege/26/68288/26.txt")

n = int(f.readline())

data = [[int(i) for i in row.split()] for row in f]


res = {
    i: 0 for i in range(15*60*60, 21*60*60)
}


for start, stop in data:
    if start < 15*60*60: start = 15*60*60
    if stop > 21*60*60: stop = 21*60*60
    
    for i in range(start, stop):
        res[i] += 1

most_common = Counter(res).most_common(1)[0][1]

counter = 0

for key, value in res.items():
    counter += value == most_common

print(most_common, counter)