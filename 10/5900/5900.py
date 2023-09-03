from string import punctuation

f = open('10/5900/5900.txt').read().upper()

for i in punctuation:
    f = f.replace(i, ' ')

slova = f.split()

glasnie = 'АЕЁИОУЫЭЮЯ'

counter = 0

for slovo in slova:
    if len(slovo) > 1:
        for bukva in glasnie:
            counter += slovo.count(bukva)

print(counter)