from ipaddress import *

ipNet = '105.224.200.224'
mask = '255.255.255.224'

# for ip in ip_network(ipNet + '/' + mask)

counter = 0

for ip in ip_network('105.224.200.224/255.255.255.224'):
    binIp = bin(int(ip))[2:]
    
    # binIp = ''.join([bin(int(i))[2:].zfill(8) for i in str(ip).split(".")])

    if binIp.count('1')%4 == 0:
        counter += 1


print(counter)