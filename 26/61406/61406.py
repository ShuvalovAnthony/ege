f = open("26/61406/26.txt")

events = sorted(
    [
    [int(i) for i in row.split()] for row in f
    ],
    key=lambda x: (x[1], x[0])
)

last_stop = 0

approvedEvents = []

for start, stop in events:
    if start > last_stop + 20:
        approvedEvents.append([start, stop])
        last_stop = stop


preLastStop = approvedEvents[-2][-1]

maxDiff = 0
for start, stop in events:
    maxDiff = max(maxDiff, start - preLastStop)

print(len(approvedEvents), maxDiff)
