def check(num: str):
    num = num.replace('1', 'N').replace('3', 'N').replace('5', 'N')
    num =num.replace('0', 'C').replace('2', 'C').replace('4', 'C').replace('6', 'C')
    if num[0] == 'N':
        res = num.replace('NC', '')
    else:
        res = num.replace('CN', '')
    return res == ''

count = 0



for a1 in ('123456'):
    for a2 in ('0123456'):
        for a3 in ('0123456'):
            for a4 in ('0123456'):
                for a5 in ('0123456'):
                    for a6 in ('0123456'):
                        num = a1 + a2 + a3 + a4 + a5 + a6
                        if (num.count('6') == 1) and check(num):
                            count += 1

print(count)
