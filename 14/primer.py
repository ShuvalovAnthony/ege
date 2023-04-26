num = 9**8*3**20 - 3**10 - 3

# cc = 18
# bukva dlya poiska C

cifri = []

while num > 0:
	cifri.append(num%100)
	num //= 100

print(cifri[::-1])
