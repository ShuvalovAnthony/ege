net_ip = "170.155.136.0"
ip_addr = "170.155.137.181"


print([bin(int(i))[2:].zfill(8) for i in net_ip.split('.')])

print([bin(int(i))[2:].zfill(8) for i in ip_addr.split('.')])


['10101010', '10011011', '10001 00 0', '00000000'] # network

['11111111', '11111111', '11111 11 0 ', '00000000'] # 2**9 - 2 # mask

['10101010', '10011011', '10001 00 1', '10110101'] # client


print("11111110", 2) # otvet