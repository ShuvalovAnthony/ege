import ipaddress


ip = [10, 18, 134, 220]
bin_ip = [bin(i)[2:].zfill(8) for i in ip]

print(bin_ip)


