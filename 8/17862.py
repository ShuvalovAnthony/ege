from itertools import *

def check(n):
    cou=0
    for i in n:
        if int(i,12)>8:
            cou+=1
    return cou<=3

coun=0
for n in product('0123456789ab',repeat=5):
    n=''.join(n)    
    if n[0] != '0' and n.count('7')==1 and check(n):
        coun+=1

print(coun)