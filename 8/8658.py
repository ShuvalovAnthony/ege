from itertools import product

index = 1

for word in product('АНП', repeat=5):
    word = ''.join(word)
    if index == 201:
        print(word, index)
    
    index += 1