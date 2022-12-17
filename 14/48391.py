def convert(num: str, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]




# yAAx.12 + x02y.14

alph = '0123456789AB'

for x in alph:
    for y in alph:
        first_num = y + "AA" + x
        second_num = x + "02" + y
        res = int(convert(first_num, 12, 10)) + int(convert(second_num, 14, 10))
        if res%80 == 0:
            print(res/80)
            

