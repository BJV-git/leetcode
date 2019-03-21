


def intersec(arr, nums):
    if not arr or not nums:
        return []
    d=set()
    res = set()
    for i in arr:
        d.add(i)
    for j in nums:
        if j in d:
            res.add(j)
    return list(res)

print(intersec([1,2,2,1],[2]))