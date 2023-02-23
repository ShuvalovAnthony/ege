f = open('9/6041/6041.txt')

# Способ 1

nums = tuple(sorted(map(int, i.split())) for i in f)

counter = 0

for i in f:
    a, b, c = i
    if (a != b != c) and (c < a + b):
        counter += 1

print(counter)


# Способ 2

# nums = [list(map(int, i.split())) for i in f]

# counter = 0

# for i in nums:
#     a, b, c = sorted(i) # c - максимальное
#     if (a != b != c) and (c < a + b):
#         counter += 1

# print(counter)