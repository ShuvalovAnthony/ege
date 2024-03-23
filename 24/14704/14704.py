f = open("24/14704/24_14704.txt").read()

def checkSubString(subS: str):
    leftFlag = True
    left = 0
    right = 0
    for i in range(len(subS) - 1):
        if (subS[i + 1] >= subS[i]) and leftFlag:
            left += 1
            continue
        else:
            leftFlag = False
        if (subS[i + 1] < subS[i]):
            right += 1
        else:
            right += 1
            return left + right


lens = set()

for i in range(len(f) - 1):
    for j in range(i + 1, i + 20):
        subS = f[i: j]
        lenSubS = checkSubString(subS)
        if lenSubS:
            lens.add(lenSubS)

    print(i)

print(max(lens))