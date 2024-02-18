f = open("3/63052/63052.txt")

data = {"М" + str(i).zfill(2):0 for i in range(100)}


for row in f:
    row = row.split()
    shop_num = row[0]
    pack_number = int(row[1])

    data[shop_num] += pack_number


max_summa = 0
shop_num_answer = 0


for shop_number, itogovaya_summa in data.items():
    if itogovaya_summa > max_summa:
        max_summa = itogovaya_summa
        shop_num_answer = shop_number


print(shop_num_answer, max_summa)