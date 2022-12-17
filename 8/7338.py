# count = 0

# for a1 in 'КАТЕР':
#     for a2 in 'КАТЕР':
#         for a3 in 'КАТЕР':
#             for a4 in 'КАТЕР':
#                 for a5 in 'КАТЕР':
#                     for a6 in 'КАТЕР':
#                         res = a1 + a2 + a3 + a4 + a5 + a6
#                         if res[0] == 'Р' and res[-1] == 'К':
#                             count += 1

# print(count)



from itertools import product
count = 0

for i in product('КАТЕР', 'КАТЕР', 'КАТЕР', 'КАТЕР', 'КАТЕР', 'КАТЕР'):
    if i[0] == 'Р' and i[-1] == 'К':
        count += 1

print(count)