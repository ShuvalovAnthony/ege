# from itertools import combinations

# p = {i for i in range(2, 21, 2)}

# q = {i for i in range(5, 51, 5)}

# vars_a = p | q


# sets_a = []

# for i in range(len(vars_a)):
#     sets_a += (list(combinations(vars_a, i + 1)))


# for a in sets_a[::-1]:
#     flag = True

#     for x in range(100):
#         if not (
#             ((x in a) <= (x in p)) or
#             ((x not in q) <= (x not in a))
#         ):
#             flag = False
#             break

#     if flag:
#         print(len(a))
#         break




from itertools import combinations

p = {1, 2, 4, 8}
q = {1, 2, 3, 4, 5, 6}

sets_a = []
default_set = p | q

for i in range(len(default_set)):
    sets_a += (list(combinations(default_set, i + 1))) # i + 1 !!!!!!


for a in sets_a:
    flag = True

    for x in range(30):
        if not (
            (x not in a) <=
            (not (
                (x in p) or
                (x in q)
            ))
        ):
            flag = False
            break

    
    if flag:
        print(len(a), a)
        break

