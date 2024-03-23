f = open("26/13101/26_13101.txt")


n = int(f.readline())

clients = sorted([
    [int(i) for i in row.split()] for row in f
], key=lambda x: x[0]
)


# t, t obsl, nomer okna / 0 - luboe


okno_1 = [] # список времен окончания обслуживания
okno_2 = []


def find_client(t: int):
    for time, timeObsluzh, okno in clients:
        if time > t:
            return False
        elif time == t:
            return time, timeObsluzh, okno

leaveCounter = 0
okno_2_counter = 0

for t in range(60*24):
    if t in okno_1:
        okno_1 = okno_1[1:]
    
    if t in okno_2:
        okno_2 = okno_2[1:]

    if find_client(t):
        time, timeObsluzh, okno = find_client(t)
        if (okno == 1):
            if (len(okno_1) < 14):
                if not okno_1:
                    okno_1.append(t + timeObsluzh)
                else:
                    okno_1.append(okno_1[-1] + timeObsluzh)
            else:
                leaveCounter += 1

        elif (okno == 2):
            if (len(okno_2) < 14):
                okno_2_counter += 1
                if not okno_2:
                    okno_2.append(t + timeObsluzh)
                else:
                    okno_2.append(okno_2[-1] + timeObsluzh)
            else:
                leaveCounter += 1

        elif (okno == 0) and (min(len(okno_1), len(okno_2)) < 14):
            if (len(okno_1) <= len(okno_2)):
                targetOkno = okno_1
            else:
                targetOkno = okno_2
                okno_2_counter += 1

            if not targetOkno:
                targetOkno.append(t + timeObsluzh)
            else:
                targetOkno.append(targetOkno[-1] + timeObsluzh)
        else:
            leaveCounter += 1
            

print(okno_2_counter, leaveCounter)