s = "АБВГД БВЕ ВЕЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛМ КМ ЛМ М"
d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

print(f('А', 'В')*f('В', 'М'))