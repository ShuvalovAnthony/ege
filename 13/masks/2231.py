# from ipaddress import IPv4Address, IPv4Network

# ip_address = IPv4Address("162.198.0.157")
# subnet_mask = IPv4Address("255.255.255.224")


# # network = IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
# network = IPv4Network(str(ip_address) + '/' + str(subnet_mask), strict=False)


# ordinal_number = int(ip_address) - int(network.network_address)


from ipaddress import ip_address

ip = ip_address('162.198.0.157')
bin_ip = bin(int(ip))[2:]

mask = ip_address('255.255.255.224')
bin_mask = bin(int(mask))[2:]

print(bin_mask)


print(bin_ip)
print(int('11101', 2))

# 2**5 == 32

# network
# mask
# ip_adress