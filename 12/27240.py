from itertools import product


def check(stroka: str):
    return (stroka.count('1') == 10) and (stroka.count('2') == 3)


def algo(stroka: str):
    while '11' in stroka:
        if '112' in stroka:
            stroka = stroka.replace('112','6',1)
        else:
            stroka = stroka.replace('11','3',1)
    return stroka


def digits_sum(stroka: str):
    return sum([int(i) for i in stroka])


max_sum = 0

for stroka in product("12", repeat=13):
    stroka = "".join(stroka)
    if check(stroka):
        max_sum = max(
            digits_sum(
                algo(stroka)
            ),
            max_sum
        )

print(max_sum)
    