s = '0' + '122'*14 + '1'*14 + '0'

while '00' not in s:
    s = s.replace('011', '20', 1)

    s = s.replace('022', '10', 1)

    s = s.replace('01', '220', 1)

    s = s.replace('02', '110', 1)


print(s, s.count('1'), s.count('2'))