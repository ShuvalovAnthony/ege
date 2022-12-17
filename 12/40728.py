min_index = 201
max_ones = 0

for i in range(201, 1000):
    s = '1'*i

    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)

    if s.count('1') > max_ones:
        max_ones = s.count('1')
        min_index = i

print(min_index)