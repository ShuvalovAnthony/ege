def convert(num: str, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]


num = 3*343**8 + 5*49**12 + 7**15 - 49 # наше число

num = convert(num, 10, 7) # число в 7ой системе счисления



for i in range(7): # для цифр от 0 до 6...
    print(i, num.count(str(i)))



answ = {} # словарь для подсчета колва цифр в виде - цифра: колво цифр в строке

for i in range(7): # для цифр от 0 до 6...
    answ[i] = num.count(str(i)) # в словарь по ключу ЦИФРА добавить значение КОЛВО ЦИФР в строке

print(answ)