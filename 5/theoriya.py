# int() - из СТРОКИ в десятичную систему, 2ой параметр - ИЗ какой системы счисления
# в результате - всегда ДЕСЯТИЧНАЯ


# bin() из десятичной в двоичную
# oct() из десятичной в восьмеричную
# hex() из десятичной в шестнадцатиричную
# срез чтобы убрать начальные 2 символа 0b 0o 0x - [2::]


# перевод из любой СС в любую СС до 36ой включительно
from string import digits, ascii_uppercase


def convert(num: str, from_base: int, to_base: int):
    num = int(str(num), from_base)
    alphabet = digits + ascii_uppercase
    answ = alphabet[num%to_base]
    while num >= to_base:
        num //= to_base
        answ += alphabet[num%to_base]
    return answ[::-1]

# Пример перевода из 16ричной в 27ричную
print(convert("AB17", 16, 27))
