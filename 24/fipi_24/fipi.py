f = open('ege/24/fipi/24.txt').readline()

# Способ 1

# answ = 0

# if f[0] in 'AO': wait_glas = False
# else: wait_glas = True


# counter = 0
# for j in range(1, len(f)):
#     if wait_glas and f[j] in 'AO':
#         counter += 1
#         wait_glas = False
#     elif not wait_glas and f[j] in 'CDF':
#         counter += 1
#         wait_glas = True
#     else:
#         answ = max(answ, counter)
#         counter = 0

# print(answ//2)



f = f.replace('O', 'A').replace('D', 'C').replace('F', 'C')



f1 = list(map(len, f.replace('AC', 'X').replace('A', ' ').replace('C', ' ').split()))
print(max(f1))


f2 = list(map(len, f.replace('CA', 'X').replace('A', ' ').replace('C', ' ').split()))
print(max(f2))


    