import time

f = open("26/10133/26_10133.txt")

data = sorted([
    [int(i) for i in row.split()] for row in f
], key=lambda x: (x[0], x[1])
)

START_TIME = time.time()

max_proc = 0

max_time = 0
curr_time = 0



for t in range(1, 10100):
    curr_proc = 0
    for start, stop in data:
        if start <= t <= stop:
            curr_proc += 1
        if start > t:
            break
    
    max_proc = max(max_proc, curr_proc)

    if curr_proc > 0:
        curr_time += 1
    else:
        max_time = max(max_time, curr_time)
        curr_time = 0

STOP_TIME = time.time()

print(max_time, max_proc, STOP_TIME - START_TIME)