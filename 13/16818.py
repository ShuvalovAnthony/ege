# s = "АБВГ БВД ВДЕГ ГИ ДЖЕК ЕКИ ЖК КЛМН ЛН МН Н"
s = "АБГ БД ГИ ДЖЕК ЕКИ ИК ЖК КЛМН ЛН МН Н"

d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

print(f('А', 'Н'))