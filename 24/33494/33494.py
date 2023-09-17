from string import ascii_uppercase

f = open('24/33494/24.txt').readline()

counter = {i: 0 for i in ascii_uppercase}

for i in range(len(f) - 1):
    if f[i] == 'E':
        counter[f[i+1]] += 1

max_freq_letter = 0
answ_letter = ''

for i in counter:
    if counter[i] > max_freq_letter:
        max_freq_letter = counter[i]
        answ_letter = i

print(max_freq_letter, answ_letter)