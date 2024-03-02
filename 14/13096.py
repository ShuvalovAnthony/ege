from itertools import product


for x, y in product(range(39), range(39)):
    digits = [9, 4, y, 3, 2, 7, x, 8, 5]
    num = 0
    for i in range(len(digits)):
        num += digits[i]*39**i
    
    if num%38 == 0:
        checkNum = y*39 + x
        if (
            (checkNum**0.5 == int(checkNum**0.5)) and 
            (checkNum > 0)
        ):
            print(checkNum)

