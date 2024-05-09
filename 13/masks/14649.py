from ipaddress import *

# [] [] [] 00011010
# print(bin(224)[2:].zfill(8))
for a in range(255, -1, -1):
    netIp = '116.242.' + str(a) + '.0'

    flag = True
    for ip in ip_network(netIp + '/255.255.255.224'):
        ip = [bin(int(i))[2:].zfill(8) for i in str(ip).split('.')]
        leftPart = ip[0] + ip[1]
        rightPart = ip[2] + ip[3]
        if not (
            leftPart.count("1") >= rightPart.count("1")
        ):
            flag = False
            break

    if flag:
        print(a)
        break