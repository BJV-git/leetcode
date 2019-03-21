

def self_div(l,r):
    res=[]
    for i in range(l,r+1):
        if '0' in str(i):
            continue
        if i < 9:
            res.append(i)
            continue
        flag = True
        n= str(i)
        for j in n:
            if i%int(j) != 0:
                flag = False
                break
        if flag==True:
            res.append(i)
    return res