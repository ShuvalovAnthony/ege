import string

f = open('24/35913/24.txt')

n_num = 10**6
stroka = ''

for i in f:
    if i.count('N') < n_num:
        n_num = i.count('N')
        stroka = i



max_kolvo = 0
letter = 'ABOBA - CHELOVEK ILI TAINA VSELENNOI?'

for j in string.ascii_uppercase: # 'ABCDEF...'

    if stroka.count(j) >= max_kolvo:
        max_kolvo = stroka.count(j)
        letter = j

print(letter)
