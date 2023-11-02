from collections import Counter
import time
import os

start = time.time()

nums = []

with open("9/6357/6357.txt") as f:
    for row in f:
        nums.append([int(i) for i in row.split()])


def check_row(row):
    repeat = []
    non_repeat = []
    for k, v in Counter(row).items():
        if v > 1:
            for _ in range(v):
                repeat.append(k)
        else:
            non_repeat.append(k)
    
    if repeat and non_repeat:
        if sum(repeat) / len(repeat) > sum(non_repeat) / len(non_repeat):
            return True
    return False 
        
c = 0


for row in nums:
    if check_row(row):
        c+=1
        
print(c)
