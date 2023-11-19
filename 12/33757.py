# s = '0' + '1111123'*10
# print(s.count('1'))

# while ('01' in s) or ('02' in s) or ('03' in s):
#     s = s.replace('01', '30', 1)
#     s = s.replace('02', '101', 1)
#     s = s.replace('03', '202', 1)

# print(s.count('1'), s.count('2'), s.count('3'))

from itertools import product

def algo(s):
    while ('01' in s) or ('02' in s) or ('03' in s):
        s = s.replace('01', '30', 1)
        s = s.replace('02', '101', 1)
        s = s.replace('03', '202', 1)

    return s



for k1, k2, k3 in product(
    range(1, 70),
    range(1, 70),
    range(1, 70),
):
    s = '0' + '1'*k1 + '2'*k2 + '3'*k3

    s = algo(s)

    if (
        s.count('1') == 20 and
        s.count('2') == 10 and
        s.count('3') == 70
    ):
        print(k1)


