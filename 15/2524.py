from itertools import combinations


'''
1 елочный шарик
2 носок
3 стеклянный шарик
4 мешок
5 гирлянда
6 сани
7 колокольчик
'''
import itertools

def get_combinations(n):
    result = []
    for r in range(1, n+1):
        for combo in itertools.combinations(range(1, n+1), r):
            result.append(list(combo))
    return result

res = []

for a in get_combinations(7):
    flag = True
    for x in (1, 2, 3, 4, 5, 6, 7):
        if not (
            ((x not in (1, 2, 3, 4, 5,)) and \
            (x not in (6, 3,7, 5))) or \
            (x in a)
        ):
            flag = False
            break

    if flag:
        res.append(a)


print(res)