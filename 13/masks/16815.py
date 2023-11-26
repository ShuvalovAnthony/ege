from ipaddress import IPv4Address
from itertools import product

ip = IPv4Address('98.162.71.94')
bin_ip = bin(int(ip))[2:]

network = IPv4Address('98.162.71.64')
bin_network = bin(int(network))[2:]

print(bin_ip)
print(bin_network)



for i in product(['0', '1'], repeat=6):
    print(''.join(i))