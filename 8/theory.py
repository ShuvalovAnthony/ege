from itertools import *


s = 'abcdoughhoooaubcddfo'

# в функцию приходит строка !!!!!!
# если используем product/permutations - обязательно
# сделать ''.join()


# 1 - нет рядом стоящих ОДИНАКОВЫХ гласных
def check1(s):
    for glas in 'eyuioa':
        if glas*2 in s: return False
    return True


# 2 - нет рядом стоящих ЛЮБЫХ гласных
def check2(s: str):
    for glas in 'eyuioa': s = s.replace(glas, '_')
    return '__' in s


# 1 - нет рядом стоящих ОДИНАКОВЫХ букв
def check3(s):
    for letter in set(s):
        if letter*2 in s: return False
    return True

# '''
#  Какое количество 6-буквенных слов вы сможете составить перестановкой букв слова «МАКАКА»?
#  В данной задаче нужно принять подходящими все возможные последовательности, вне зависимости
#    имеет или нет данный набор букв смысловое содержание. При этом необходимо избегать слов 
#    с двумя подряд одинаковыми буквами.
#  '''

# correctWords = set()
# for word in permutations("МАКАКА", 6):
#     word = ''.join(word)
#     if check3(word):
#         correctWords.add(word)

# print(correctWords)
# print(len(correctWords))