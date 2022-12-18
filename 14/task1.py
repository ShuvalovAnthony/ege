# for x in range(0, 37):
#     num1 = 1*37**3 + 2*37**2 + 3*37 + x
#     num2 = 4*37**3 + x*37**2 + 5*37 + 9
#     summa = num1 + num2
#     if summa%36 == 0:
#         print(x)


import string

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

alphabet = string.digits + string.ascii_uppercase + '_'

nums = {}

for i in range(1000000):
    num_digits = numberToBase(i, 37)
    res = ''
    for digit in num_digits:
        res += alphabet[digit]
    nums[res] = i


for x in alphabet:
    key1 = '123' + x
    key2 = '4' + x + '59'
    summa = nums[key1] + nums[key2]
    if summa%36 == 0:
        print(summa//36)
