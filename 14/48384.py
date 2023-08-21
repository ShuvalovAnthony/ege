from string import digits

def convert(num: str, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]


# 88x4y + 7x44y
alph = digits[:9]

for x in alph:
    for y in alph:
        first_num = '88' + x +'4' + y
        second_num = '7' + x + '44' + y
        res = (int(convert(first_num, 9, 10)) + int(convert(second_num, 11, 10)))
        if res%61 == 0:
            print(res//61)
            break