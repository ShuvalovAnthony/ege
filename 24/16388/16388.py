f = open("24/16388/24_16388.txt").read()


for i in range(100, 0, -1):
    if "KLMN"*i in f:
        maxLen = i
        break

s = maxLen * "KLMN"

varsLeft = ['LMN', 'MN', 'N', '']
varsRight = ['KLM', 'KL', 'K', '']


for vL in varsLeft:
    for vR in varsRight:
        subS = vL + s + vR
        if subS in f:
            print(len(subS))

        