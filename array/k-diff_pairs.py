# as the difference is abs, they can be either of the both sides
# learned frm other: go once for finding the counter

def kdiff(nums,k):

    count=0
    d={}
    for i in nums:
        d[i] = d.get(i,0)+1

    for i in d:
        if k >0 and i+k in d or k==0 and d[i]>1:
            count+=1
    return count

print(kdiff([3,1,4,1,5],2))