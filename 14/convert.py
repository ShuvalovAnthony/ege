def convert(num: str, from_base: int, to_base: int):
	num = int(str(num), from_base)
	alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
	answ = alphabet[num%to_base]
	while num >= to_base:
			num //= to_base
			answ += alphabet[num%to_base]
	return answ[::-1]


print(convert(49**8 + 7**24 - 7, 10, 7).count('0'))

