s = "ЭЛВ ВАБГ АБГ БДЕ ГЕЖ ДИЛЕ ЖЕ ИЛ КЖ ЛКЖ Е"
d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

print(f('Э', 'Е'))