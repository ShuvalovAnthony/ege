def convert(num: str, from_base: int, to_base: int):
	num = int(str(num), from_base)
	alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
	answ = ''
	while num > 0:
			answ += alphabet[num%to_base]
			num //= to_base
	return answ[::-1]


# начинаем с 1 т.к. x - стоит в самом левом разряде и не может быть 0 (незначащим)
for x in '123456789ABCDEFGHIJKL': 
	for y in '0123456789ABC':
		res = (
			int(convert(x + '23' + x + '5', 22, 10)) - 
	        int(convert('67' + y + '9' + y, 13, 10))
        )
		if res%57 == 0:
			print(x, y, res//57)
