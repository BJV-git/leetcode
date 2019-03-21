# logic: said it got added, by random shuffle
# means no set, as not sure if single or duped

# using xor

def diff(s,t):
    d={}
    ans=0
    for c in s+t:
        ans^=ord(c)
    return chr(ans)
    for i in s:
        d[i] = d.get(i,0)+1

    for j in t:
        try:
            d[j]-=1
        except:
            return j
    res=[i for i,j in d if j!=0]
    return res[0]