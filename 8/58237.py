from itertools import product

counter = 0


def check(num: tuple):
    for i in range(1, len(num)):
        if num[i] >= num[i - 1]: return False
    return True



for num in product(range(7), repeat=4):
    if (
        check(num) and
        (num[0] != 0)
    ):
        counter += 1

print(counter)

