from ipaddress import ip_address
from itertools import permutations


for i in permutations(['7.2', '53', '102.', '84.1'], 4):
    addr = ''.join(i)
    try:
        ip_address(addr)
        print(addr)
    except:
        ...