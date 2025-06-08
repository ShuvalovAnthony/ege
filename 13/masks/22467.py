from ipaddress import ip_network, ip_address


ip = ip_address('192.214.116.184')


for mask in range(33):
    net = ip_network(f'192.214.116.184/{mask}', strict=False)

    bin_net = f'{int(net[0]):032b}'
    
    if bin_net.count('1')%5 == 0:
        if net[0] < ip < net[-1]:
            print(bin_net)



print([bin(int(i))[2:].zfill(8) for i in "192.214.116.184".split('.')])


['11000000', '11010110', '01110100', '10111 000']


['11111111', '11111111', '11111000', '11111 000']