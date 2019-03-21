


def intrsction(arr, nums):
    if not arr or not nums:
        return []
    d={}
    res = []
    for i in arr:
        d[i] = d.get(i,0)+1

    for j in nums:
        try:
            d[j]-=1
            res.append(j)
        except:
            pass
    return res