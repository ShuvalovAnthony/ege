def convert(num: str, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]




for a in range(1, 1000):
    for x in '012345678':
        m = int(convert('842' + x + '5', 9, 10))
        n = int(convert('8' + x + '725', 9, 10))

        if (m + a)%n == 0:
            print(a)
        
