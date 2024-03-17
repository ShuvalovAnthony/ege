from itertools import product


f = open("22/13097/13097.txt")

# 8	0	82      ID START STOP
data = sorted([
    [int(i) for i in row.split()] for row in f
], key=lambda x: (x[1], x[2])
)

