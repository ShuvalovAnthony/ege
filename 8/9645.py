from itertools import product


index = 1

for word in product('ВЛТУ', repeat=4):
    print(''.join(word), index)
    index += 1