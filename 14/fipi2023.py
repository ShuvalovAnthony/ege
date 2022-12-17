def convert(num: str, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]


# 0 - 9 A B C D E

for x in '0123456789ABCDE':
    num_10 = int(convert(('123' + x + '5'), 15, 10)) + int(convert(('1' + x + '233'), 15, 10))
    if num_10%14 == 0:
        print(num_10//14)