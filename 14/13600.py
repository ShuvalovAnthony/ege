num = 4**255 + 2**255 - 255

bin_num = bin(num)[2:]

print(bin_num.count('1'))
