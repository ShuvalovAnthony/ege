from itertools import product

f = open("vars/dosrok2024/22/22.txt")


rawData = [
    [int(i) for i in row.split()] for row in f
]


def cookData(rawData):
    data = {}
    for processData in rawData:
        
        if len(processData) == 4: id, duration, depProc1, depProc2 = processData
        else: id, duration, depProc1, depProc2 = *processData, None
        if depProc1 and depProc2: start = max(data[depProc1][1], data[depProc2][1]) + 1
        elif depProc1: start = data[depProc1][0] + 1
        else: start = depProc2

        data[id] = [start, start + duration - 1]

    return data

print(rawData)

def findMaxTime(data):
    maxTime = 0
    currentTime = 0
    for time in range(30):
        procCounter = 0
        for processId in data:
            start, stop = data[processId][0], data[processId][1]
            if (start <= time <= stop): procCounter += 1

        if procCounter == 4: currentTime += 1
        else:
            maxTime = max(maxTime, currentTime)
            currentTime = 0
    return maxTime
        

maxTime = 0

for t1, t2, t9, t10 in product(range(30), repeat=4):
    rawData[0][-1] = t1
    rawData[1][-1] = t2
    rawData[8][-1] = t9
    rawData[9][-1] = t10
    tempTime = findMaxTime(cookData(rawData))
    if tempTime > maxTime:
        maxTime = tempTime
        lastData = cookData(rawData)


print(maxTime)
print(lastData)
