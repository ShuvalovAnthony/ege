# a = '0' + '12' + '2211'*2 + '12'*5 + '0'

a = '0' + '12' + '2211'*2 + '12'*5 + '0'

while '00' not in a:
    a = a.replace('012', '30', 1)
    if '011' in a:
        a = a.replace('011', '20', 1)
        a = a.replace('022', '40', 1)
    else:
        a = a.replace('01', '10', 1)
        a = a.replace('02', '101', 1)

print(a, '----', a.count('1'), a.count('2'), a.count('3'))

if (a.count('1') == 7) and (a.count('2') == 5):
    print(a, a.count('3'))