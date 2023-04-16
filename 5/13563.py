counter = 0

def check(num):
    num = str(num)
    for i in '02468':
        if i in num: return False
    return True

for num in range(1000, 10000):
    num = str(num)
    sum1_2 = int(num[0]) + int(num[1])
    sum3_4 = int(num[2]) + int(num[3])

    spisok = sorted([sum1_2, sum3_4])
    res = str(spisok[0]) + str(spisok[1])

    if res == '616' and check(num):
        counter += 1
    
print(counter)