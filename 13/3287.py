s = "АБВГД БЕЖВ ВЖЗ ГЗД ДЗИ ЕЖ Ж ЗЖКИ ИК КЕЖ"

d = {i[0]:i[1:] for i in s.split()}

def f(a, b):
    return (a == b) + sum(f(c, b) for c in d[a])

print(f('А', 'Ж'))