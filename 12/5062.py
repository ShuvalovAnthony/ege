from itertools import product
from functools import lru_cache


@lru_cache
def algo(stroka: str):
    while '00' not in stroka:
        stroka = stroka.replace('011', '20', 1)
        stroka = stroka.replace('022', '10', 1)
        stroka = stroka.replace('02', '110', 1)
        stroka = stroka.replace('01', '220', 1)
    return stroka


@lru_cache
def check(stroka: str):
    return stroka.count('1') == stroka.count('2')


@lru_cache
def check_answ(stroka: str):
    return (stroka.count('1') == 47) and (stroka.count('2') < 70)


for i in range(50):
    print(i)
    for stroka_ in product('12', repeat=i*2):
        stroka = '0' + ''.join(stroka_) + '0'
        if check(stroka):
            result_stroka = algo(stroka)
            if check_answ(result_stroka): 
                print(result_stroka.count('2'))
            
            


