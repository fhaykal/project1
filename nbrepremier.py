from math import sqrt 

def premier(n):
    if n in [0,1]:
        return False
    for d in range (2,int(sqrt(n))+1):
        if n%d==0:
            return False
    return True

