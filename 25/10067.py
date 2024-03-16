cubes = [i**3 for i in range(5, 10)]

def dels(num: int):
    count = 0
    max_del = 0
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            count += 2
            max_del = max(max_del, num//i)
    
    if num**0.5%1 == 0: count -= 1
    return count, max_del


limit = 5

for num in range(10**9, 0, -1):
    if limit == 0: break
    count, max_del = dels(num)
    if (count + 2) in cubes:
        print(num, max_del)
        limit -= 1