f = open('10/5900/5900.txt').read().upper()

znaki_prep = ".,!?:;-_'\""

for i in znaki_prep:
    f = f.replace(i, ' ')

slova = f.split()

glasnie = 'АЕЁИОУЫЭЮЯ'

counter = 0

for slovo in slova:
    if len(slovo) > 1:
        for bukva in glasnie:
            counter += slovo.count(bukva)

print(counter)
