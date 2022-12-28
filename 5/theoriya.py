# int() - из СТРОКИ в десятичную систему, 2ой параметр - ИЗ какой системы счисления
# в результате - всегда ДЕСЯТИЧНАЯ


# bin() из десятичной в двоичную
# oct() из десятичной в восьмеричную
# hex() из десятичной в шестнадцатиричную
# срез чтобы убрать начальные 2 символа 0b 0o 0x - [2::]


# функция по переводу из любой в любую*
def convert(num: str, from_base: int, to_base: int):
    num = int(str(num), from_base)
    alphabet = '0123456789ABCDEFGHIJKLMNOPQ'
    answ = alphabet[num%to_base]
    while num >= to_base:
            num //= to_base
            answ += alphabet[num%to_base]
    return answ[::-1]
