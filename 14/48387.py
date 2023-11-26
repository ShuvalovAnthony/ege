from string import digits


alph = digits + 'A'


for x in alph:
    for y in alph:
        num1 = int(x + '341' + y, 11)
        num2 = int('56' + x + '1' + y, 19)

        if (num1 + num2)%305 == 0:
            print((num1 + num2)//305)