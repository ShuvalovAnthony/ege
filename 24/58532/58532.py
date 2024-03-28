f = open("24/58532/24.txt").read()


# f = "BADZXYZKLMENYZXXX"

def check(triplet: str):
    return triplet.count("X") == triplet.count("Y") == triplet.count("Z") == 1

checkList = [0]*len(f)

for i in range(len(f) - 2):
    subString = f[i:i + 3]

    if check(subString):
        checkList[i:i + 3] = [1]*3
        

result = ""

for i in range(len(f)):
    if checkList[i] == 1: result += ' '
    else: result += f[i]

print(max(
    [len(i) for i in result.split()]
))