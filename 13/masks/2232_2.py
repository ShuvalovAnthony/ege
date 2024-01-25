ip = [10, 18, 134, 220]
bin_ip = [bin(i)[2:].zfill(8) for i in ip]

mask = [255, 255, 255, 192]
bin_mask = [bin(i)[2:].zfill(8) for i in mask] 

print(bin_ip)
print(bin_mask)


for i in range(64):
    if bin(i)[2:].zfill(6) == "011100":
        print(i)