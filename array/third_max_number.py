#logic: if len < 3 return the max, if not return the third ? distinct

def thirdMax(nums):
    opt=list(set(nums))
    if len(opt)<3:
        return opt[0]
    return opt[2]
