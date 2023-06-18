f = open('24/8166/24_8166.txt').read()

counter = 0
temp_counter = 0

for i in f:
    if i in 'ABC':
        temp_counter += 1
    else:
        counter = max(temp_counter, counter)
        temp_counter = 0
    
print(counter//2)