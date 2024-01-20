from collections import Counter


def to9(n: int):
    digits = ''
    while n > 0:
        digits += str(n%9)
        n //= 9
    return digits[::-1]


def mostCommon(n: str):
    counts = Counter(n).most_common()
    max_count = counts[0][1]
    res = counts[0][0]
    for pair in counts[1:]:
        if pair[1] == max_count: res = pair[0]
        else:
            return res
    return res


for n in range(10000, 0, -1):
    n_9 = to9(n)

    for i in range(5):
        if n_9.count('5') == n_9.count('7'):
            n_9 += n_9[-1]
        else:
            n_9 += mostCommon(n_9)
    
    res_10 = int(n_9, 9)
    res_16 = hex(res_10)

    if 'bac' in res_16:
        print(n)
        break