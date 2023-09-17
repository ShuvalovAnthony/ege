f = open('24/27698/zadanie24_2.txt').read()


# способ 1

f = f.replace('D', ' ').replace('R', ' ')

print(
    max(
        [len(i) for i in f.split()]
    )
)


# способ 2

# max_dlina = -1
# tmp_dlina = 0

# for letter in f:
#     if letter == 'L':
#         tmp_dlina += 1
#     else:
#         max_dlina = max(max_dlina, tmp_dlina)
#         tmp_dlina = 0

# print(max_dlina)