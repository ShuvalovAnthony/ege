from ipaddress import IPv4Network


for mask in range(33):
    net = str(IPv4Network('224.128.112.142/' + str(mask), strict=False))

    if '224.128.64.0' in net:
        print(mask)


print(int('11000000', 2))

