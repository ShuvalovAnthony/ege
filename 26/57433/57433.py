f = open('26/57433/1_26.txt')

k = int(f.readline())
n = int(f.readline())

times = sorted(
    [[int(j) for j in i.split()] for i in f],
    # key=lambda x: (x[0], x[1])
)

slots = [-1]*k
counter = 0
last_slot = 0


for start, stop in times:
    for slot_num in range(k):
        if start >= slots[slot_num]:
            counter += 1
            slots[slot_num] = stop + 1
            last_slot = slot_num
            break

print(counter, last_slot + 1)