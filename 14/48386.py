alphabet = '0123456789ABCDE'

for x in alphabet:
    for y in alphabet:
        result = int('90' + x + '4' + y, 15) +\
                int('91' + x + y + '2', 16)
        
        if result%56 == 0:
            print(result//56)
