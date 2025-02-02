
ip_1 = "206.123.209.193"
ip_2 = "206.123.210.118"



print([bin(int(i))[2:].zfill(8) for i in ip_1.split('.')])
print([bin(int(i))[2:].zfill(8) for i in ip_2.split('.')])


['11111111', '11111111', '111111 00', '00000000']


['11001110', '01111011', '110100 01', '11000001']
['11001110', '01111011', '110100 10', '01110110']

counter = 0

for i in range(1, 2**10 - 1):
    left = "1100111001111011110100"
    right = bin(i)[2:].zfill(10)

    ip = left + right

    if ip.count("1") == 15:
        counter += 1

print(counter)