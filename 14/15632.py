num = 4**14 + 2**32 - 4

answ = bin(num)[2::]

print(answ.count('1'))