# n - натуральное
def f(n):
    if n < 3: # 1 2
        return 1
    
    if n % 2 != 0: # 3 5 7 9 ...
        return f(n-1) + 3 * f(n-2)
    
    # 4 6 8 10.....
    s = []
    for i in range(1, n):
        s.append(f(i))
    return sum(s)
    
print(f(28))    