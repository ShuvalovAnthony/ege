from itertools import product


for i in product('CONST', repeat=16): # tuple
    word = ''.join(i) # str
    print(word)

