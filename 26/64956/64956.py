f = open("ege/26/64956/26.txt")

n = int(f.readline())


clients = sorted([
    [int(i) for i in row.split()] for row in f
])


# время освобождения окна без учета ожидания
windows = {
    i: [] for i in range(1, 7) 
}


leavers = 0

for start, duration, window in clients:
    if (not windows[window]):
        windows[window].append(start + duration)
    elif (windows[window][-1] <= start + 30):
        windows[window].append(
            max(windows[window][-1], start) + duration
            )
    else:
        leavers += 1


print(
    min([len(windows[i]) for i in range(1, 7)]),
    leavers
)