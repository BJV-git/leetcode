# just need to look extra case is that, if k is higher then need ot look for dup

# can use the dict to update by the elements we move on

# learned: just store the recent occuring numerb index and if encountered a number <=k return True

def hasdup_in_k(nums,k):
    d={}
    for i, num in enumerate(nums):
        if num in d:
            if i - d[num] <= k:
                return True
        d[num]=i


    return False

print(hasdup_in_k([1,2,3,1],3))