from ipaddress import IPv4Address
from itertools import permutations

def check(ip_str):
    try:
        IPv4Address(ip_str)
        return True
    except:
        return False


for ip in permutations(['24.12', '1.96', '4.2', '17'], 4):
    ip_str = ''.join(ip)
    if check(ip_str):
        print(ip)
