#logic: map and see
# 

def can_return(s):
    dic={'U':[0,1], 'R':[1,0], 'L':[-1,0], 'D':[0,-1]}
    res=[0,0]

    for i in s:
        res[0]+= dic[i][0]
        res[1]+=dic[i][1]

    return res==[0,0]

print(can_return('UD'))