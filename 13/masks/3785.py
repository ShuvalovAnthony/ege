mask = bin(224)[2:]

bits = mask.count('0')

ip_vars = 2**bits - 2

print(ip_vars)