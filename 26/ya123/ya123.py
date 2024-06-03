with open('26/ya123/26.txt') as f:
    w, k = map(int, f.readline().split())
    times = [int(i) for i in f.readlines()]

times = sorted(times)
workers = {i: [] for i in range(w)}
    
for i in range(len(times)):
    for k, v in workers.items():
        if (not v) or (times[i] >= v[-1] + 60):
            v.append(times[i])
            break
        else:
            continue



minlen = 10 ** 11

for el in workers.values():
    minlen = min(minlen, len(el))



print(minlen, sum([len(i) for i in workers.values()]))