s = "абвг бд вде гвеи дкл едлжи жлм ижмн кпм лкм мпсрн нр пс рс с"
starts = "абвгдежиклмнпр"
d = {i[0]:i[1:] for i in s.split()}

f = lambda a, b: (a == b) +\
      sum(f(c, b) for c in d[a])

summa = 0
for i in starts:
    summa += f(i, 'с')
print(summa)