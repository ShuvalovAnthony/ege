# # start_n ----> res_n = 55

# for n in range(100): # n = 0
#     start_n = n


#     n = 550

#     res_n = n**2

#     if res_n == 64:
#         print(start_n)
#         break

# n = int(input('vvedite chislo '))

# print(bin(n)[2::]) # binary - бинарный - двоичный - на выходе str
# print(oct(n)[2::]) # oct - восмеричная - на выходе str
# print(hex(n)[2::]) # hex - 16ти ричная - на выходе str



# print(int('AaaaFFBB2134234234', 16))
# print(hex(3148268265387415781940))


# функция перевода из любой в любую систему счисления
def convert(num: str, from_base: int, to_base: int):
		num = int(str(num), from_base)
		alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
		answ = alphabet[num%to_base]
		while num >= to_base:
				num //= to_base
				answ += alphabet[num%to_base]
		return answ[::-1]

# print(convert('60345526', 7, 2))




