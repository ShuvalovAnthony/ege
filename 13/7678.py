s = "аБГ БГЕВ ВАЖ ГД ДЕБ ЕЗВ ЖА ЗВЖ"

d = {i[0]:i[1:] for i in s.split()}

def f(a, b):
    return a[-1] == b or sum(f(a +c, b) for c in d[a[-1]] if c not in a)

print(f('а', 'А'))