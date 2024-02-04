from ipaddress import *


count = 0
for a in range(0, 256):
    flag = True
    network = ip_network('207.0.' + str(a) + '.167/255.255.255.192', strict=False)

    for addr in network:
        addr = [bin(int(i))[2:].zfill(8) for i in str(addr).split('.')]
        addr_left = addr[0] + addr[1]
        addr_right = addr[2] + addr[3]

        if not (addr_left.count('0') > addr_right.count('0')):
            flag = False

    if flag:
        count += 1

print(count)



# from ipaddress import *


# count = 0
# for a in range(0, 256):
#     flag = True
#     network = ip_network('207.0.' + str(a) + '.167/255.255.255.192', strict=False)
#     for ip in network:
#         ip_netwk = str(ip).split('.')
#         lev = bin(int(ip_netwk[0]))[2:].zfill(8).count('0') + bin(int(ip_netwk[1]))[2:].zfill(8).count('0')
#         prav = bin(int(ip_netwk[2]))[2:].zfill(8).count('0') + bin(int(ip_netwk[3]))[2:].zfill(8).count('0')
#         if lev <= prav:
#             flag = False
#     if flag:
#         count += 1

# print(count)