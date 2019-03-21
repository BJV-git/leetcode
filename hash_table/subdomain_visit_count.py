


import collections
def visit(domains):
    dic={}
    res=[]

    for d in domains:
        c, name=d.split(' ')
        c=int(c)
        temp = name.split('.')

        while temp:
            t  = '.'.join(temp)
            dic[t] = dic.get(t,0)+c
            a=temp.pop(0)


    for i in dic:
        res.append(str(dic[i]) + ' '+ i)
    return res

