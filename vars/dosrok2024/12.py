def algo(s: str):
    while ("1111" in s) or ("7777" in s):
        if "1111" in s:
            s = s.replace("1111", "77", 1)
        else:
            s = s.replace("7777", "11", 1)
    return s


def summaCifr(s: str):
    return sum([int(i) for i in s])

maxSum = 0

for n in range(4, 10000):
    s = "7" + "1"*n
    resS = algo(s)
    tempSum = summaCifr(resS)
    if tempSum >= maxSum:
        print(tempSum, resS)
        maxSum = tempSum

print(maxSum)