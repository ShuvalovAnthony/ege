from itertools import product, permutations, combinations


def check(num: str):
    kolvo_nechetnih = 0
    for digit in num:
        if digit in '1357':
            kolvo_nechetnih += 1

    if (
        (num[0] != '0') and
        (num.count('4') == 1) and
        (kolvo_nechetnih == 2)
    ):
        return True
    
    return False


counter = 0

for num in product(
    '012345678', repeat=6
):
    num = ''.join(num)
    counter += check(num)


print(counter)
