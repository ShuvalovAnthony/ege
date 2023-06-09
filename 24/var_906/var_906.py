f = open('24/var_906/24.txt').read()


max_len = -1

last_start = 0

def chet(num:str):
    return num in '02468'

def nechet(num:str):
    return num in '13579'

last_digit = '2'

start = 0

for i in range(len(f)):
    if f[i] in '0123456789':
        if chet(f[i]) and chet(last_digit):
            start = i
        elif chet(f[i]) and nechet(last_digit):
            max_len = max(max_len, i - start + 1)
            start = i
        elif nechet(f[i]) and nechet(last_digit):
            start = i
        elif nechet(f[i]) and chet(last_digit):
            max_len = max(max_len, i - start + 1)
            start = i
        last_digit = f[i]

print(max_len)