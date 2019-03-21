# lets have an i which represents normal flow and other
# dict for the given one

# other way is to sort and go sequentially can easily find the missing and dup

# lets combien both

def mismatchset(nums):
    repeated=0
    missing=0
    dic={}
    d={}
    j=1
    for i in nums:
        d[j] = 1
        j+=1
        dic[i] = dic.get(i,0)+1

    for i in d:
        diff = dic.get(i,0) - d[i]
        if diff == 1: # repeated
            repeated=i
        if diff==-1:
            missing=i
    return [repeated, missing]