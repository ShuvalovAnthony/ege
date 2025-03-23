net = "122.159.136.144"

mask = "255.255.255.248"


bin_net = [bin(int(i))[2:].zfill(8) for i in net.split('.')]
bin_mask = [bin(int(i))[2:].zfill(8) for i in mask.split('.')]

# print(bin_net)
# print(bin_mask)



counter = 0

for i in range(2**3):
    right = bin(i)[2:].zfill(3)
    if (15 + right.count("1"))%4 != 0:
        counter += 1

print(counter)