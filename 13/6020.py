# s = "АБГВ БГД ВГЗ ГДЕЖЗ ДИЕ ЕИКЖ ЖЛ ЗЖЛ ИМК КМ ЛКМ М"
s = "АБГВ БГД ВГЗ ГДЕЗ ДИЕ ЕИК ЗЛ ИМК КМ ЛКМ М"
d = {i[0]:i[1:] for i in s.split()}


# def f(a, b):
#     return (a == b) + sum(f(c, b) for c in d[a])

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

print(f('А', 'М'))