# Дано число 19010585582505 в 
# десятичной сколько в нем A в 13тиричной

num = 19010585582505
cifri = []

while num > 0:
    cifri.append(num%13)
    num //= 13

cifri = cifri[::-1]


print(cifri.count(10))



# Способ 2

alphabet = '0123456789ABC'

num = 19010585582505
cifri = []

while num > 0:
    cifri.append(alphabet[num%13]) # 0...12
    num //= 13

cifri = ''.join(cifri[::-1])

print(cifri)
print(cifri.count('A'))




# from string import digits, ascii_lowercase

# alphabet = digits + ascii_lowercase[:22]

# print(alphabet)