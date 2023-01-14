f = open('ege/24/35284/24.txt')

strings = [i.strip() for i in f]

min_g = 10**6
most_common_letter = ''
string_with_less_g = ''


def most_common_letter(s:str):
    import string
    max_count = 0
    res_letter = ''
    for letter in string.ascii_uppercase:
        if s.count(letter) >= max_count:
            max_count = s.count(letter)
            res_letter = letter
    return res_letter


for string in strings:
    if string.count('G') < min_g:
        min_g = string.count('G')
        string_with_less_g = string


print(most_common_letter(string_with_less_g))