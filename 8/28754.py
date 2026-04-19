# from itertools import product


# index = 1

# for word in product(sorted("АПРЕЛЬ"), repeat=5):
#     word = ''.join(word)

#     if (
#         (index%2 == 0) and
#         (word[0] not in "ЬР") and
#         (word.count("Л") >= 2)
#     ):
#         print(index, word)

#     index += 1

num = 2*2187**567 + 4325345345


counter = 0


while num > 0:
    if (num%27)%2 == 0 and (num%27 > 10):
        counter += 1

    num //= 27

print(counter)