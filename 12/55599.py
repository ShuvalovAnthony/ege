from itertools import product


def algo(s):
    while '00' not in s:
        s = s.replace('02', '101')
        s = s.replace('11', '2')
        s = s.replace('12', '21')
        s = s.replace('010', '00')
    return s


def prime(s):
    n = sum([int(i) for i in s])
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True



for i in range(70, 100):
    # for word in product('12', repeat=i):
    #     if word.count('1') == word.count('2'):
            # s = '0' + ''.join(word) + '0'
    s = '0' + '1'*i + '2'*i + '0'

    s = algo(s)

    if prime(s):
        print(i)
        break


