f = open("26/60967/26_59852.txt")

n = int(f.readline())
k = int(f.readline())

details = []
containers = []

for i in range(n + k):
    if i < n: details.append(int(f.readline()))
    else: containers.append(int(f.readline()))
    

totalVolume = 0
count = 0

for detail in details:
    for i in range(len(containers)):
        if detail <= containers[i]:
            totalVolume += detail
            count += 1
            containers[i] -= detail
            break

print(totalVolume, count)