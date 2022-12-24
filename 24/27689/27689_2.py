f = open('24/27689/24.txt').readline()

f = f.replace('XYZXY', '5').replace('XYZX', '4').replace('XYZ', '3')

f = f.replace('X', ' ').replace('Y', ' ').replace('Z', ' ').split()




counter = 0
max_dlina = 0

for i in range(len(f)):
    if f[i] == '3':
        counter += 3
    elif f[i] == '4' and counter != 0:
        counter += 4
        max_dlina = max(max_dlina, counter)
        counter = 0
    elif f[i] == '5' and counter != 0:
        counter += 5
        max_dlina = max(max_dlina, counter)
        counter = 0


print(max_dlina)