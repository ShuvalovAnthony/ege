f = open("24/15339/24_15339.txt").read()


for i in "ABC":
    f = f.replace(i, "A")


for i in "6789":
    f = f.replace(i, "0")


for i in range(100, 0, -1):
    if ('A0'*i in f):
        subString = "A0"*i
        break

vars = [
    '0' + subString + 'A',
    '0' + subString,
    subString + 'A',
    subString
]

for var in vars:
    if var in f:
        print(len(var))
        break