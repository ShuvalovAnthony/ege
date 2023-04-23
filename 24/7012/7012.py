f = open('24/7012/24_7012.txt')

counter = 0

def qwerty(s: str) -> str:
    least = list('QWERTY') # [  ']
    for i in s:  
        try:
            if i == least[0]:
                least.remove(i)
        except:
            pass
    return least == []

for stroka in f:
    for i in 'UIOPASDFGHJKLZXCVBNM0123456789':
        stroka = stroka.replace(i, '')
    if qwerty(stroka): counter += 1

print(counter)