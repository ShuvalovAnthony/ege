from ipaddress import IPv4Network, IPv4Address


# print([bin(int(i))[2:].zfill(8) for i in '175.184.48.0'.split('.')])
# print(['11111111', '11111111', '11111000', '00000000'])
# print([bin(int(i))[2:].zfill(8) for i in '175.184.52.103'.split('.')])

ip = IPv4Address('175.184.52.103') # ip который ищем в сети
for i in range(32, -1, -1): # i - колво единиц в маске
    try:
        # сеть в зависимости от маски
        net = IPv4Network("175.184.48.0/" + str(i)) 
        
        # если ip в сети - пишем i
        if ip in net:
            print(i)
            break
        
    except:
        ...

print(bin(123)[2:].zfill(8))