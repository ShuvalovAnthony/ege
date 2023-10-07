s = "АБ БВГ ВДГЕ ГЕ ДЁЗГ ЕИЖ ЁЙ ЖК ЗЁЙН ИНКЖ ЙЛ КМ ЛН МН НО О "
d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

print(f('А', 'О'))