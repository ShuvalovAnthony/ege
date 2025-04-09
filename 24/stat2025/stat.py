from re import findall


f = open("ege/24/stat2025/24.txt").read()


pat = r'(?:0|[1-5][0-5]*)' + r'(?:[*](?:0|[1-5][0-5]*))*' + r'(?:[-](?:0|[1-5][0-5]*))*'
exps = findall(pat, f)


max_len = 0
max_exp = ''
for exp in exps:
    if len(exp) > max_len:
        max_len = len(exp)
        max_exp = exp


print(max_len, max_exp)