from string import ascii_uppercase

f = open('24/33526/33526.txt').read()

letters = {i: 0 for i in ascii_uppercase}

for i in range(1, len(f) - 1):
    if f[i - 1] == f[i + 1]:
        letters[f[i]] += 1

reverse_letters = {val: key for key, val in letters.items()}

print(reverse_letters[max(reverse_letters)])
