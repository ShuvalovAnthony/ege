syst_schisl = 7

num = 177

digits = []


while num > 0:
    digits.append(num%syst_schisl)
    num //= syst_schisl

digits = digits[::-1]

print(digits)