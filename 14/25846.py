def convert(num: any, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]


num = (9**8)*(3**20) - 3**10 - 3

answ = convert(num, 10, 3)

print(answ.count('2'))