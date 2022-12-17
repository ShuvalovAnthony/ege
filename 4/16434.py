# 'АБГИНРТ'
# Г 110
# И 01
# Т 10

# А 000
# Б 001
# Н 1110
# Р 1111

combos = ['110', '01', '011' '10', '000', '001', '1110', '1111']

def check(s1, s2):
    if len(s1) < len(s2):
        return s1 == s2[:len(s1)]
    return s2 == s1[:len(s1)]


for i in range(len(combos)):
    for j in range(i + 1, len(combos)):
        print(check(combos[i], combos[j]), i, j)


for i in range(50):
    print(bin(i)[2:])