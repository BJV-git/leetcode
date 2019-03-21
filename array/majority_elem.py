# logic: is the one which appears n//2 times so obvious only one


def majority(nums):

    ln = len(nums)
    t=ln//2

    d={}
    for i in nums:
        d[i] = d.get(i,0)+1
        if d[i] > t:
            return i
