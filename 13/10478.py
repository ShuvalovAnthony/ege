s = "АБВГД БЕВ ВЕЖЗ ГВЗ ДГЗ ЕЖИ ЖИ ЗЖИ ИЛ ЛМ М"

d = {i[0]:i[1:] for i in s.split()}

def f(a, b):
    return (a == b) + sum(f(c, b) for c in d[a])


print(f('А', 'Ж')*f('Ж', 'М'))