# logic: all we need to find is the number which has difference is 1 and both has min - max diff 1
# no way we can hev the other as the diff gonna change


def LHS(nums):
    d={}
    for i in nums:
        d[i] = d.get(i,0)+1

    r=[[i,j] for i,j in d.items()]

    r.sort(key=lambda x: [x[0],x[1]])
    maxi=0
    lr = len(r)
    for i in range(lr-1):
        if r[i+1][0]-r[i][0] ==1:
            maxi = max(r[i][1]+r[i+1][1], maxi)

    return maxi