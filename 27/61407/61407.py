k, n, *a = map(int, open('27/61407/27-B.txt')) 

b = {x: a.count(x) for x in sorted(a)[::-1][:3]} 

back = m = float('-inf')

for i in range(2*k, n): 
    back = max(back, a[i-2*k])
    any_mx = max(x for x in b if (b[x] - (a[i] == x) - (back == x)) > 0) 
    m = max(m, back + any_mx + a[i]) 
print(m)