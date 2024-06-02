from itertools import product, permutations

k = 4

def check(s):
    return (s.count("1") == 23*k) and (s.count("2") == 4*k) and (s.count("3") == 13*k)



origS = '1'*2*k + '2'*4*k + '3'*3*k

for s in permutations(origS):
    s = '0' + ''.join(s) + '0'

    while '00' not in s:
        s = s.replace("01", "103", 1)
        s = s.replace("02", "2011", 1)
        s = s.replace("03", "130", 1)


    if check(s):
        print(123)
        break


 