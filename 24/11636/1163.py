from string import ascii_uppercase

f = open("24/11636/24_11636.txt").read()

a_indexes = []

for i in range(len(f)):
    if f[i] == "A":
        a_indexes.append(i)

'''
a_indexes = [1 3 5 7 8 9 10]
            0 1 2  3 4 5 6
'''

counter = 0

for i in range(1, len(a_indexes)):
    if a_indexes[i] - a_indexes[i - 1] > 1:
        counter += i
    else:
        counter += i - 1

print(counter)



