from itertools import product

min_count = 10

for x in product('12', repeat = 20):
    s = ''.join(x)
    s = '0' + s + '0'
    st = s
    if s.count('1') == 10 and s.count('2') == 10:
        while '00' not in s:
            s = s.replace('012', '30', 1)
            if '011' in s:
                s = s.replace('011', '20', 1)
                s = s.replace('022', '40', 1)
            else:
                s = s.replace('01', '10', 1)
                s = s.replace('02', '101', 1)
    if s.count('1') == 7 and s.count('2') == 5:
        if s.count('3') < min_count:
            min_count = s.count('3')
            m_s = st

        
print(min_count, m_s)

# for i  in range(1, 100):
#     a = '0' + '1'*i + '2'*i + '0'

#     while '00' not in a:
#         a = a.replace('011', '20', 1)
#         a = a.replace('022', '10', 1)
#         a = a.replace('01', '220', 1)
#         a = a.replace('02', '110', 1)

#         if (a.count('1') == 40) and (a.count('2') > 50):
#             print(a.count('2'))


        