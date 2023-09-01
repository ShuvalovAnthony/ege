import ipaddress

adresses = ipaddress.IPv4Network('192.168.32.160/255.255.255.240')

counter = 0

for adress in adresses:
    bin_adress = bin(int(adress))[2:]
    if bin_adress.count('1')%2 == 0: counter += 1


print(counter)