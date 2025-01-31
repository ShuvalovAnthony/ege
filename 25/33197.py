def check(num: int):
    counter = 0
    for delitel in range(int(num**0.5), 0, -1):
        if counter == 3: break
        if num%delitel == 0:
            if ((num//delitel - delitel) <= 100):
                counter += 1
    
    return counter >= 3



for num in range(10**6, 2*10**6 + 1):
    if check(num): print(num)
