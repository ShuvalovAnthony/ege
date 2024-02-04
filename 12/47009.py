 
for n in range(50):
    for m in range(50):
        for k in range(50):
            s = '0' + n * '1' + m * '2' + k * '3' + '0'

            while not('00' in s):
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)

            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(n + m + k + 2)