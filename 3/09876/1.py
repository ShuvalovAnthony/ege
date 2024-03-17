f = open("3/09876/1.txt")

data = [
    [int(i) for i in row.split()] for row in f
]

res = {i: [] for i in range(150)}

for id, _, mark in data:
    res[id].append(mark)


counter = 0

for _, marks in res.items():
    if marks and (sum(marks)/len(marks) >= 4):
        counter += 1
    
print(counter)
    