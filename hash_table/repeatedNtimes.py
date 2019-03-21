

def ntimes(A):
    d={}
    la = len(A)
    target = la//2
    for i in A:
        d[i] = d.get(i,0)+1
        if d[i]==target:
            return i