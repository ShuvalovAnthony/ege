from ipaddress import *

ip = IPv4Interface('10.18.134.220')
bin_ip = bin(int(ip))[2:].zfill(32)

mask = IPv4Interface('255.255.255.192')
bin_mask = bin(int(mask))[2:].zfill(32)

print(bin_mask, len(bin_mask))


print(bin_ip)



print(int('011100', 2))