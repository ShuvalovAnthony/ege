from collections import Counter


f = open("24/55641/55641.txt")

most_common_letters = ''

def mostCommonLetterAfterT(row: str):
    res = ''
    letters = ''
    for i in range(len(row) - 1):
        if row[i] == 'T':
            letters += row[i + 1]
    
    max_counter = Counter(letters).most_common(1)[0][1]
    for letter in set(letters):
        if letters.count(letter) == max_counter:
            res += letter

    return res


for row in f:
    most_common_letters += mostCommonLetterAfterT(row)

max_counter = Counter(most_common_letters).most_common(1)[0][1]
print(max_counter)