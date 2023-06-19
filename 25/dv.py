from fnmatch import fnmatch


def check(num):
    kolvo_delitelei = 0
    for i in range(1, num + 1):
        if num%i == 0: kolvo_delitelei += 1
    for stepen_dvoiki in range(31):
        if 2**stepen_dvoiki == kolvo_delitelei: return True
    return False



for i in range(31*2031, 10**9 + 1, 31*2031):
    if fnmatch(
        str(i), '*31*65'
    ):
        if check(i):
            print(i, i//2031)