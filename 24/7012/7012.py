f = open('24/7012/24_7012.txt')

counter = 0

# первый способ - ПЛОХОЙ по качву кода
def qwerty(s: str) -> str:
    least = list('QWERTY')
    for i in s:  
        try:
            if i == least[0]:
                least.remove(i)
        except:
            pass
    return least == []


# второй способ ХОРОШО
def qwerty2(s: str) -> str:
    q = 'QWERTY'
    for i in s:
        if not q: return True
        if i == q[0]:
            q = q[1::]
    return not q


for stroka in f:
    if qwerty2(stroka): counter += 1

print(counter)