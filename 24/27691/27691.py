# # Способ 1

# f = open('24/27691/zadanie24_1.txt').readline()


# max_dlina = 0
# counter = 0
# for i in range(len(f)):
#     if f[i] == 'A':
#         counter += 1
#     else:
#         max_dlina = max(max_dlina, counter)
#         counter = 0

# print(max_dlina)



print(max(map(len, open('24/27691/zadanie24_1.txt').readline().replace('B', ' ').replace('C', ' ').split())))



