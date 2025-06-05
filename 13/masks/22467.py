from ipaddress import ip_network, ip_address


ip = ip_address('192.214.116.184')


for mask in range(33):
    net = ip_network(f'192.214.116.184/{mask}', strict=False)

    bin_net = f'{int(net[0]):032b}'
    
    if bin_net.count('1')%5 == 0:
        if net[0] < ip < net[-1]:
            print(bin_net)