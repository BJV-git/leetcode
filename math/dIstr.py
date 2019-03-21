# LOGIC: lets fill i with the normal flow and d with the reverse flow incrementaly

def dIstr(s):
    lend = len(s)
    # print(lend)
    inc = 0
    dec = lend
    res=[]
    for i in s:
        if i=='D':
            res.append(dec)
            dec-=1
        else:
            res.append(inc)
            inc+=1
    if s[-1]=='I':
        res.append(inc)
    else:
        res.append(dec)
    return res
print(dIstr("DDIDIIIIDI"))
