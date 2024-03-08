f = open("26/61372/26.txt")

events = sorted(
    [
    [int(i) for i in row.split()] for row in f
    ],
    key=lambda x: (x[1], -x[0])
)

# print(events)
events_counter = 0
last_stop = 0
last_delta = 0

for start, stop in events:
    if start > last_stop + 15:
        events_counter += 1
        last_delta = start - last_stop
        last_stop = stop
    
print(events_counter, last_delta)