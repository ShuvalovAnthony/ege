"""
В терминологии TCP/IP маской сети называют двоичное число,
 которое показывает, какая часть IP-адреса узла сети относится 
 к адресу сети, а какая  — к адресу узла в этой сети. Адрес
   сети получается в результате применения поразрядной 
   конъюнкции к заданному адресу узла и маске сети. Сеть
     задана IP-адресом 192.168.32.160 и маской сети
       255.255.255.240. Сколько в этой сети IP-адресов,
         для которых сумма единиц в двоичной записи 
         IP-адреса чётна?

В ответе укажите только число.
"""


from ipaddress import IPv4Network


net = IPv4Network("192.168.32.160/255.255.255.240")

count = 0

for adress in net:
    bin_adress = bin(int(adress))[2:]
    summa_ed = bin_adress.count('1')
    if summa_ed%2 == 0:
        count += 1

print(count)


print('-'*20)


print(bin(160)[2:].zfill(8))
print(bin(240)[2:].zfill(8))