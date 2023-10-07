s = "АБГ БД ВДБАГЖ ГЖ ДИЕ еВЛ ЖЕ ИЛ КЖ ЛКЖ Е"

d = {i[0]:i[1:] for i in s.split()}

def f(a, b):
    return (a == b) + sum(f(c, b) for c in d[a])

print(f('е', 'Е'))