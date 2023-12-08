# count = 0


# def check(word):
#     for combo in (
#         '15', '51', '35', '53', '75', '57'
#     ):
#         if combo in word:
#             return False
#     return True


# for a1 in '12345678':
#     for a2 in '012345678':
#         for a3 in '012345678':
#             for a4 in '012345678':
#                 for a5 in '012345678':
#                     word = a1 + a2 + a3 + a4 + a5

#                     if (word.count('5') == 1) and check(word):
#                         count += 1

# print(count)



from itertools import product
from string import digits, ascii_lowercase

alph = digits[:9]
counter = 0

def check(word):
    for combo in (
        '15', '51', '35', '53', '75', '57'
    ):
        if combo in word:
            return False
    return True


for word in product(alph, repeat=5):
    word = ''.join(word)
    if (
        (word.count('5') == 1) and
        (word[0] != '0') and
        check(word)
    ):
        counter += 1

print(counter)