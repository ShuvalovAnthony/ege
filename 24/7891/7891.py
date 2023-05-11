from string import ascii_uppercase, digits

f = open('24/7891/24_7891.txt').read()


max_dlina = 0

for i in (ascii_uppercase + digits):
    temp_max_dlina = max(len(i) for i in f.split(i))
    max_dlina = max(max_dlina, temp_max_dlina + 2)

print(max_dlina)