from time import time


f = open('ege/26/41001/26.txt')

n = int(f.readline())

times = []

start_time = 1634515200

max_time = 0

for i in f:
    start, stop = map(int, i.split())
    if stop < start_time:
        pass
    else:
        times.append((start, stop))
        max_time = max(max_time, start, stop)

process_counter = {}

max_counter = 0


for current_sec in range(1634515200, max_time + 1):
    counter = 0
    for start, stop in times:
        if ((start == 0 and stop >= current_sec) or
        (start <= current_sec and stop >= current_sec) or
        (start <= current_sec and stop == 0)):
            counter += 1
    max_counter = max(max_counter, counter)


print(max_counter)

