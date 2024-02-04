# from itertools import product


# for n in range(20, 35):
#     for s in product('12', repeat=n):
#         s = '0' + ''.join(s) + '0'
#         if s.count('1') == s.count('2'):
#             while '00' not in s:
#                 s = s.replace('011', '20', 1)
#                 s = s.replace('022', '10', 1)
#                 s = s.replace('01', '220', 1)
#                 s = s.replace('02', '110', 1)
            
#             print(s, s.count('1'), s.count('2'))
#             if (s.count('1') == 40) and (s.count('2') > 50):
#                 print(s.count('2'))


