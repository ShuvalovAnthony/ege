f = open('10/63059/63059.txt').read().lower()




letters = 'дaюeгрtвщwхyчиslнbцdжыgpтъакэoмясьзйуёопuеrmhcф4лбniш'

for letter in set(f):
    if letter in letters:
        f = f.replace(letter, "😃")
    else:
        print(letter)
        f = f.replace(letter, " ")


counter = 0

for word in f.split():
    if len(word) == 4:
        counter += 1

print(counter)