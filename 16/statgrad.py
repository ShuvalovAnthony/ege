
a = 237567892
b = 1134567004

print((b - a)//3)

counter = 0
num = 28219251773445778 # 237567892

for i in range(237567893, 1134567004+1):
    if num%3: counter += 1
    num += i
    if i%10**6 == 0: print(i, 'i')


print(counter)




10 - 1
21 - 0
33 - 0