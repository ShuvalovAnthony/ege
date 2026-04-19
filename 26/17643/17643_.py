f = open("ege/26/17643/26_17643.txt")
k = int(f.readline())
s = 0

all_data = {}

for row in f:
    articl, price, state = [int(i) for i in row.split()]
    
    if articl not in all_data:
        all_data[articl] = [price, 1-state, state]
    else:
        all_data[articl][1] += (1-state) 
        all_data[articl][2] += state


new_data = []
prices = []
for articl,info in all_data.items():
    prices.append(info[0])
    if info[0]>553.96:
        new_data.append([articl, *info])
new_data = sorted(new_data, key=lambda x: [
    x[2],
    x[1],
    -x[3]
])
print(new_data)