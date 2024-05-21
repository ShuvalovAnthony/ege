f = open("10/ya/1/1.txt").read().lower()

    
''' из Из'''

counter = 0
for word in f.split():
    if 'из' in word and len(word) > 2:
        print(word)
        counter += 1

print(counter)