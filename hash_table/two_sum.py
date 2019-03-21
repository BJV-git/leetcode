


def two_sum(nums, target):
    d={}
    j=0
    for i in nums:
        print(d)
        t = target-i
        if t in d:
            return [j, d[t]]
        d[i] =j
        j+=1

    return None

print(two_sum([2,7,11,15],9))