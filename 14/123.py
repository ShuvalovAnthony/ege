def convert(num: str, from_base: int, to_base: int):
    num = int(str(num), from_base)
    alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
    answ = alphabet[num%to_base]
    while num >= to_base:
            num //= to_base
            answ += alphabet[num%to_base]
    return answ[::-1]



# 123 (x) + 1 (10) = 101 (7)


for x in range(4, 16):
    if int(convert(121, x, 10)) + 1 == int(convert(101, 7, 10)):
        print(x)
