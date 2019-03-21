

def hasalter(n):
    if n <0:n += 2**32
    n = bin(n)[2:]
    if len(n)==1:
        return True
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            return False
    return True