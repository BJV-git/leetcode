def findDuplicates( nums):
    opt = {}
    for i in nums:
        if i in opt.keys():
            opt[i] += 1
        else:
            opt[i] = 1
    return [i for i, j in opt.items() if j > 1]

print(findDuplicates([4,3,2,7,8,2,3,1]))