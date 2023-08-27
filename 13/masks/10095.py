import ipaddress

network_address = ipaddress.IPv4Network('192.168.32.160/255.255.255.240')


count = 0
for ip in network_address:
    binary_ip = bin(int(ip))[2:]  # Преобразуем IP-адрес в двоичное представление
    ones_count = binary_ip.count('1')  # Считаем количество единиц в двоичном представлении
    if ones_count%2 == 0:  # Проверяем, чётное ли количество единиц
        count += 1

print(count)
