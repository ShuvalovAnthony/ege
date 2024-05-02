f = open("26/60268/26_2024.txt")

n = int(f.readline())

events = sorted(
    [
    [int(i) for i in row.split()] for row in f
    ],
    key=lambda x: (x[1], x[0])
)

last_stop = 0
last_delta = 0

approvedEvents = []

for i in range(len(events)):
    start, stop = events[i][0], events[i][1]
    if start >= last_stop:
        approvedEvents.append(events[i])
        last_stop = stop
    

preLastStop = approvedEvents[-2][-1]

maxDiff = 0
for start, stop in approvedEvents:
    maxDiff = max(maxDiff, start - preLastStop)

print(len(approvedEvents), maxDiff)