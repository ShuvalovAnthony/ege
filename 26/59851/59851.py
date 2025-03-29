f = open("26/59851/26_6759.txt")

n = int(f.readline())

prices = sorted([int(i) for i in f], reverse=True)
# n = 7

# prices = [7, 6, 5, 4, 3, 2, 1]

# prices = [7, 5, 4,    6, 3, 2,      1] -> [, 5, 4, , 3, 2, 1]

# prices = [7, 5, 3,      6,  4,  2,          1] 

len_discount = n//3

plan = sum(prices[len_discount:])
fact = sum(prices) - sum(prices[2::3])


print(plan, fact)

