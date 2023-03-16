f = open('10/4322/4322.txt').read().lower()

words = f.split()

counter = 0

for word in words:
    if (
        ('в' in word) and 
        ('а' not in word) and 
        ('о' not in word)  
    ): counter += 1

print(counter)