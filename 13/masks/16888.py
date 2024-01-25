net = [98, 162, 71, 64]
bin_net = [bin(i)[2:].zfill(8) for i in net]


ip = [98, 162, 71, 95]
bin_ip = [bin(i)[2:].zfill(8) for i in ip]


print(bin_net)
print(bin_ip)