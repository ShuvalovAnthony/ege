def check(num: int):
    counter = 0
    for delitel in range(1, int(num**0.5) + 1):
        if num%delitel == 0:
            if ((num//delitel - delitel) <= 100):
                counter += 1
    
    return counter >= 3



for num in range(10**6, 2*10**6 + 1):
    if check(num): print(num)
