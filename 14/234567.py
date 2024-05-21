from string import *

alf = digits + ascii_uppercase[:19]


for x in alf:
    ari = int('42' + x + '158', 29) + int('16' + x + '234', 29)
    if ari%28==0:
        print(ari/28)
        break