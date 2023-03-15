from itertools import product


def check(word):
    if word[-1] == 'G' or word[0] == 'G': return False
    for i in ('GG', 'OO', 'LL'):
        if i in word: return False
    
    for i in range(1, len(word) - 1):
        if word[i] == 'G':
            srez = word[i - 1: i + 2]
            if (srez != 'OGL') and (srez != 'LGO'):
                return False
            
    return True

answ = {}

for repeat_counter in range(1, 13): # 13 !!!
    counter = 0
    for i in product('GOL', repeat=repeat_counter):
        word = ''.join(i)
        if check(word):
            counter += 1
    answ[repeat_counter] = counter


print(answ)

for i in range(13, 21): # 13 со строки 19!!!
    answ[i] = answ[i - 2] + answ[i - 1]

print(answ)
print('Otvet', answ[20])