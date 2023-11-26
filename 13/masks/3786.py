from ipaddress import IPv4Address, IPv4Network

ip_address = IPv4Address("232.126.150.18")
subnet_mask = IPv4Address("255.255.240.0")


# network = IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
network = IPv4Network(str(ip_address) + '/' + str(subnet_mask), strict=False)


ordinal_number = int(ip_address) - int(network.network_address)

print(ordinal_number)
