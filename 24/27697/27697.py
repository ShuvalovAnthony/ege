f = open("24/27697/zadanie24_2.txt").read()

# 1 sposob
# max_dlina = 0

# temp_dlina = 15

# for letter in f:
#     if letter == 'D':
#         temp_dlina += 1
#     else:
#         max_dlina = max(max_dlina, temp_dlina)
#         temp_dlina = 0


# print(max_dlina)


# 2 sposob
f = f.replace('L', ' ').replace('R', ' ')

print(
    max(
        [len(i) for i in f.split()]
    )
)

