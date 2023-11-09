from itertools import combinations

sets_a = []
default_set = {1, 2, 3, 4, 5, 6, 9, 12}


for i in range(len(default_set)):
    sets_a += (list(combinations(default_set, i)))


for set_a in sets_a:
    flag = True

    for x in range(1, 30):
        if not (
            (not (
                (x not in set_a) and
                (x in {3, 6, 9, 12})
            )) or
            (not (
                x in {1, 2, 3, 4, 5, 6}
            ))
        ):
            flag = False
            break

    
    if flag:
        print(len(set_a), set_a)
        break

