def f(start, stop, step): # 0p 1v 2p 3v                 2
    if start >= 55:
        if (
            ((start <= 77) and (step == 2)) or
            ((start > 77) and (step == 1))
            ): return True
        else: return False
    
    if step % 2 == 0:
        return f(start+3, stop, step+1) and f(start*2, stop, step+1) and f(start*3, stop, step+1)
    else:
        return f(start+3, stop, step+1) or f(start*2, stop, step+1) or f(start*3, stop, step+1)
    
    
for s in range(1, 55):
    if f(s, 55, 0):
        print(s)   

