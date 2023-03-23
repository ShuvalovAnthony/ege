def check(num):
    num = str(num)
    if ('0' in num) or (len(num)%2): return False
    
    left = num[:len(num)//2]
    right = num[-(len(num)//2):]
    summ_left = sum(list(map(int, left)))
    summ_right = sum(list(map(int, right)))
    
    return summ_left == summ_right


# 999 999 999 999 9

# 32* *** *54 ?12 3

symbols = [''] + [str(i) for i in range(10)]
nums = set()

for star1 in symbols:
    for star2 in symbols:
        for star3 in symbols:
            for star4 in symbols:
                for star5 in symbols:
                    for q in '0123456789':
                        res = int(
                            '32' + star1 + star2 +\
                            star3 + star4 + star5 + '54' +\
                            q + '123'
                        )
                        nums.add(res)

for num in nums:
    if check(num) and (num%519 == 0) and (num < 10**13):
        print(num, num//519)
                        





