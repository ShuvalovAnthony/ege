s = 'АБГВ БГД ВГ ГДЕИ ДЖЕ ЕИК ЖН ИК КМ МП НП П'

d = {i[0]:i[1:] for i in s.split()}

def f(a, b):
    return (a == b) + sum(f(c, b) for c in d[a])

print(f('А', 'Е')*f('Е', 'П'))