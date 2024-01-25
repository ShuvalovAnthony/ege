from ipaddress import IPv4Address
from itertools import permutations

def check(ip_str):
    try:
        IPv4Address(ip_str)
        return True
    except:
        return False


for ip in permutations(['3.212', '21', '2.12', '.42'], 4):
    ip_str = ''.join(ip)
    if check(ip_str):
        print(*ip)





# 2 sposob


# for ip in permutations(['.64', '3.13', '3.133', '20'], 4):
#     ip_str = ''.join(ip)
#     try:
#         IPv4Address(ip_str)
#     except:
#         ...

