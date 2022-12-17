s = '0' + '1'*6 + '2'*32 + '3'*2

while ('01' in s) or ('02' in s) or ('03' in s):
    s = s.replace('01', '2302', 1)
    s = s.replace('02', '10', 1)
    s = s.replace('03', '201', 1)


print(s.count('1'), s.count('2'), s.count('3'))

