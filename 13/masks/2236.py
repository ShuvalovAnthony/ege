from ipaddress import ip_address


mask = ip_address("255.255.254.0")
bin_mask = bin(int(mask))[2:]

# 1111111110000
print(bin_mask)


print(
    2**bin_mask.count('0') - 2
)
