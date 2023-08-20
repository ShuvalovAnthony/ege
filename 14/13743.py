num = 49**10 + 7**30 - 49
syst_schisl = 7

digits = []

while num > 0:
    digits.append(num%syst_schisl)
    num //= syst_schisl

digits = digits[::-1]

print(digits.count(6))
