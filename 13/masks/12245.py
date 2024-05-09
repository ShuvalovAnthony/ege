from ipaddress import ip_network

counter = 0

for addr in ip_network("192.168.32.48/255.255.255.240"):
    bin_addr = bin(int(addr))[2:]

    if bin_addr.count('1')%2:
        counter += 1

print(counter)

