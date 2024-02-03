from ipaddress import IPv4Network


net = IPv4Network("112.154.133.208/255.255.252.0", strict=False)

counter = 0
for addr in net:
    addr = [bin(int(i))[2:].zfill(8) for i in str(addr).split('.')]
    addr_left = addr[0] + addr[1]
    addr_right = addr[2] + addr[3]

    if (
        (addr_left.count('1') <= addr_right.count('0')) and
        (addr_right.count('0')%2)
    ):
        counter += 1

print(counter)