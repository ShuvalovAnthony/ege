from itertools import product


def check(word):
    if word[-1] == 'S' or word[0] == 'S': return False
    for i in ('CC', 'OO', 'NN', 'SS', 'TT'):
        if i in word: return False
    
    for i in range(1, len(word) - 1):
        if word[i] == 'S':
            if word[i - 1] == word[i + 1]: return False

    return True

answ = {}

for repeat_counter in range(1, 10): # 10 !!!
    counter = 0
    for i in product('CONST', repeat=repeat_counter):
        word = ''.join(i)
        if check(word):
            counter += 1
    answ[repeat_counter] = counter


print(answ)

for i in range(5, 17): # 10 со строки 19!!!
    answ[i] = (answ[i - 1] + answ[i -2])*3 # строим формулу по закономерности из предыдущего вывода

print(answ)
print('Otvet', answ[16])