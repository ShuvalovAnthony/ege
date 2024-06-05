from itertools import product

stopList = []

for i in product('0246', repeat=2):
    stopList.append(''.join(i))
for i in product('1357', repeat=2):
    stopList.append(''.join(i))



def check(num: str):
    for i in stopList:
        if i in num: return False
    return True

counter = 0

for num in product("0234567", repeat=5):
    num = ''.join(num)
    if len(num) == len(set(num)) and num[0] != '0':
        counter += check(num)

print(counter)