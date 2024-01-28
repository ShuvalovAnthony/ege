from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:9]


for x in alph[::-1]:
    res = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
    if res%18 == 0:
        print(res//18)
        break