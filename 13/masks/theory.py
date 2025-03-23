# for i in range(1, 33):
#     mask = ('1'*i).zfill(32)[::-1]
#     mask = [mask[:8], mask[8:16], mask[16:24], mask[24:]]
#     int_mask = [int(i, 2) for i in mask]
#     print(mask, int_mask)




# ip_addr = "255.255.255.0"

# bin_ip_addr = [bin(int(i))[2:].zfill(8) for i in ip_addr.split('.')]

# from_bin_to_int_ip = [int(i, 2) for i in bin_ip_addr]

# print(bin_ip_addr)
# print(from_bin_to_int_ip)



for i in range(9):
    mask = ('1'*i).zfill(8)[::-1]
    # print(mask)

    print(int(mask, 2))