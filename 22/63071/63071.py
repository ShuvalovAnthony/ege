from itertools import product

f = open("22/63071/63071.txt")


rawData = [
    [int(i) for i in row.split()] for row in f
]


def cookData(rawData):
    data = {}
    for processData in rawData:
        if len(processData) == 4: id, duration, depProc1, depProc2 = processData
        else: id, duration, depProc1 = processData

        if depProc1 and depProc2: start = max(data[depProc1][1], data[depProc2][1]) + 1
        elif depProc1: start = data[depProc1][0] + 1
        else: start = depProc2

        data[id] = [start, start + duration - 1]

    return data



def findMaxTime(data):
    maxTime = 0
    currentTime = 0
    for time in range(200, 400):
        procCounter = 0
        for processId in data:
            start, stop = data[processId][0], data[processId][1]
            if (start <= time <= stop) and (processId != 8): procCounter += 1

        if procCounter == 4: currentTime += 1
        else:
            maxTime = max(maxTime, currentTime)
            currentTime = 0
    return maxTime
        

maxTime = 0

for t1, t2 in product(range(100, 300), repeat=2):
    rawData[0][-1] = t1
    rawData[1][-1] = t2
    # rawData[7][-1] = t8
    # rawData[8][-1] = t9
    tempTime = findMaxTime(cookData(rawData))
    if tempTime > maxTime:
        maxTime = tempTime
        lastData = cookData(rawData)


print(maxTime)
