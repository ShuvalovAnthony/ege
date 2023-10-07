from ipaddress import IPv4Network


for mask in range(33):
    net = str(IPv4Network('111.81.208.27/' + str(mask), strict=False))

    if '111.81.192.0' in net:
        print(mask)