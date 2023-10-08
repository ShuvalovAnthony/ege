from ipaddress import IPv4Address, IPv4Network

ip_address = IPv4Address("162.198.0.157")
subnet_mask = IPv4Address("255.255.255.224")


# network = IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
network = IPv4Network(str(ip_address) + '/' + str(subnet_mask), strict=False)


ordinal_number = int(ip_address) - int(network.network_address)


txt = input('введите текст ')

if txt.islower:
    print('В тексте есть большие буквы')