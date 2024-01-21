from itertools import combinations

sets_a = []
default_set = {1, 3, 5, 6, 7, 9, 11, 12}


for i in range(len(default_set) + 1):
    sets_a += (list(combinations(default_set, i)))


for set_a in sets_a:
    flag = True

    for x in range(1, 30):
        if not (
            (
                (x in {1, 3, 5, 7, 9, 11}) <=
                (x not in {3, 6, 9, 12})
            ) or
            (
                x in set_a
            )
        ):
            flag = False
            break

    
    if flag:
        print(sum(set_a), set_a)
        break

