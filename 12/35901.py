
# s = '0' + '1'*2 + '2'*43 + '3'*5


# while ('01' in s) or ('02' in s) or ('03' in s):
#     s = s.replace('01', '2302', 1)
#     s = s.replace('02', '10', 1)
#     s = s.replace('03', '201', 1)

# print(s.count('1'), s.count('2'), s.count('3'))


# 50 12 7


for c1 in range(1, 50):
    for c2 in range(1, 50):
        for c3 in range(1, 50):

            s = '0' + '1'*c1 + '2'*c2 + '3'*c3

            while ('01' in s) or ('02' in s) or ('03' in s):
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)

            if s.count('1') == 50 and \
                s.count('2') == 12 and \
                    s.count('3') == 7:
                    print(c1)
