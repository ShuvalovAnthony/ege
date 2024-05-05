from itertools import product


def check(num: str):
    for i in "012345678":
        num = num.replace(i*2, '')
    return len(num) == 5


def check2(num: str):
    for i in "012345678":
        if i*2 in num: return False
    return True


counter = 0

for num in product("012345678", repeat=5):
    num = "".join(num)
    if (
        num.count("5") == 1 and
        check2(num) and 
        num[0] != '0'
    ):
        counter += 1

print(counter)