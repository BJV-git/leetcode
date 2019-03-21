# logic: return the longest, else can split and return teh longest

def LUS(a,b):
    alen=len(a)
    blen=len(b)

    if alen!=blen:
        return max(alen, blen)

    if a==b:
        return -1

    return alen