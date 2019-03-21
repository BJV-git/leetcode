

def uncommon_words(A,B):
    A=A.split(' ')
    B=B.split(' ')
    res=[]

    d={}
    for i in A:
        d[i] = d.get(i,0)+1

    for i in B:
        d[i] = d.get(i,0)+1

    for i in d:
        if d[i]==1:
            res.append(i)

    return res