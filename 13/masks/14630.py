net = "153.202.16.32"

ip = "153.202.16.37"


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]


print(bin_net)
print(bin_ip)