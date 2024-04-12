from ipaddress import ip_network

counter = 0
for ip in ip_network("222.63.131.128/255.255.255.192"):
    bin_ip = bin(int(ip))[2:]
    if bin_ip.count("0")%5 == 0:
        counter += 1
        print(bin_ip, len(bin_ip))

print(counter)



