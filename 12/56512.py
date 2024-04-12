from itertools import product

def algo(s: str):
    while "00" not in s:
        if "011" in s: s = s.replace("011", '101', 1)
        else:
            s = s.replace("01", '40', 1)
            s = s.replace("02", '20', 1)
            s = s.replace("0222", '1401', 1)

    return s


results = set()

for i in range(1, 10):
    for a in product("12", repeat=2*i):
        if (a.count('1') == a.count('2')):
            a = '0' + ''.join(a) + '0'
            
            a = algo(a)

            if (a.count('1') == 6) and (a.count('2') == 9):
                print(a.count('4'), a)
                results.add(a.count('4'))
        
print(min(results))