# counter = 0


# for a1 in 'ПЯТНИЦА':
#     for a2 in 'ПЯТНИЦА':
#         for a3 in 'ПЯТНИЦА':
#             for a4 in 'ПЯТНИЦА':
#                 for a5 in 'ПЯТНИЦА':
#                     word = a1 + a2 + a3 + a4 + a5

#                     if (
#                         (word[0] != 'Н') and
#                         (word.count('Я') == 1)
#                     ):
#                         counter += 1


# print(counter)


from itertools import product

counter = 0
for word in product('ПЯТНИЦА', repeat=5):
    if (
        (word[0] != 'Н') and
        (word.count('Я') == 1)
    ):
        counter += 1


print(counter)
