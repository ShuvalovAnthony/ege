from itertools import product

count = 0
for i in product('1234', repeat=5):
    if i.count('1') == 2:
        count += 1

print(count)