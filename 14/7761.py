print(bin(4**2020 + 2**2017 +-15)[2:].count('0'))



num = 4**2020 + 2**2017 +-15
num = bin(num)[2:]
print(num.count('1'))