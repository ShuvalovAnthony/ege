from math import sin, cos, radians


f = open("ege/27/stat2025/b.txt")

data = [
    [float(i) for i in row.split()] for row in f
]


clasters = [[]]*6

for x, y in data:
    dy = -7 - y
    dx = abs()