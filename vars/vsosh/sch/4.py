n = int(input()) 

def f(n, result): 
    if n == 0:  return result 
    elif n // 10 == 0: left = [1, 1, 1, 2, 2, 3, 3, 4, 3, 3][n] 
    else: 
        left = 1 
        right = n 
        while right - left > 1: 
            mid = (left + right) // 2 
            left += (mid - left) * (mid  <= (n + 1) // 2) 
            if left != mid: 
                right = mid 
    return f(n - left, result + [left]) 


print(*reversed(f(n, [])))