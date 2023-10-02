num = 8**888 + 15*15**1515 - 2**444

num_8 = oct(num)[2:]


counter = 0

for i in '123456':
    counter += num_8.count('7' + i)

print(counter)