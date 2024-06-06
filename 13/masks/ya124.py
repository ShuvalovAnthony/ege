from ipaddress import ip_network


network = list(ip_network("192.168.76.160/255.255.255.240"))

counter = 0

for i in range(2, len(network), 2): # только четные адреса 
    ip = network[i]
    right_byte = int(str(ip).split('.')[-1])
    bin_right_byte = bin(right_byte)[2:]

    if bin_right_byte.count("1")%2 == 0: counter += 1

print(counter)