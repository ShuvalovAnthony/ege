f = open("ege/26/14679/26_14679.txt")


n = int(f.readline())
k = int(f.readline())
print(k)
timestamps = []

def toMin(timestamp: str):
    day, month, hour, minute = [int(i) for i in timestamp.split(".")]
    totalMinutes = (month - 1)*30*24*60 + (day - 1)*24*60 + hour*60 + minute
    return totalMinutes

min_start = 10**6
max_stop = 0

for row in f:
    start, stop = [toMin(i) for i in row.split()]
    timestamps.append((start, stop))

    min_start = min(min_start, start)
    max_stop = max(max_stop, stop)

print(min_start, max_stop, len(timestamps))


busCounter = [0]*(max_stop + 1)

k = 1

for start, stop in timestamps:
    for i in range(start, stop + 1):
        busCounter[i] += 1

    k += 1
    if k%100 == 0: print(k)


primes = 0
max_buses = 0
isPrime = False

f2 = open("ege/26/14679/data.txt", mode="w")

for buses in busCounter:
    f2.write(str(buses) + '\n')

f2.close()

print(primes, max(busCounter))


