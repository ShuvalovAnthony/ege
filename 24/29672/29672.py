f = open('24/29672/inf_22_10_20_24.txt')



counter = 0

for stroka in f:
    if stroka.count('E') > stroka.count('A'):
        counter += 1

print(counter)

