# simple logic: just need to see if the numbers are available or not and return if not
# Also can find the set of given and the best possible answer to give the max possible first missing positive number and subtarct them.
# which avoids checking all the time


def firstMissingPositive( nums):
    max_num = len(set(nums))+1
    res = list(set(range(1,max_num)) - set(nums))
    print(res)

    if len(res) == 0:
        return max_num
    else:
        return sorted(res)[0]

    # nums = set(nums)
    # res = 1
    # while res in nums:
    #     res += 1
    # return res


print(firstMissingPositive([10,4,16,54,17,-7,21,15,25,31,61,1,6,12,21,46,16,56,54,12,23,20,38,63,2,27,35,11,13,47,13,11,61,39,0,14,42,8,16,54,50,12,-10,43,11,-1,24,38,-10,13,60,0,44,11,50,33,48,20,31,-4,2,54,-6,51,6]))