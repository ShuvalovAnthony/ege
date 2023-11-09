# from itertools import combinations

# p = set()
# q = set()
# a = set()

# for i in range(256):
#     n_bin = bin(i)[2:].zfill(8)
#     if n_bin[:2] == '11': p.add(i)
#     if n_bin[-1] == '0': q.add(i)
#     if (i not in p) and (i not in q): sets_a.add(i)

# a = p|q
# sets_a = set()
# for i in a:
#     if (i not in p) and (i not in q): sets_a.add(i)

# print(sets_a)

# counter = 0


# for set_a in sets_a:
#     flag = True

#     for x in range(256):
#         if not (
#             (x not in set_a) <=
#             (
#                 (x in p) or
#                 (x not in q)
#             )
#         ):
#             flag = False
#             break

    
#     if flag:
#         counter += 1


# print(counter)
