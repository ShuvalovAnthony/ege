from string import ascii_lowercase

s = 'IUHFbjkdsfnsduigBHJKFBDSfnuisdkjfshuybYUGBHJFsdnfdsfbsdfuidsfa'.lower()


letter_counter = {i: 0 for i in ascii_lowercase}

for letter in s:
    letter_counter[letter] += 1

for _, value in letter_counter.items():
    print(value)
