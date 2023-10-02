alph = '0123456789AB'

for x in alph:
    for y in alph:
        first_num = y + "AA" + x
        second_num = x + "02" + y
        res = int(first_num, 12) + int(second_num, 14)
        if res%80 == 0:
            print(res/80)
            

