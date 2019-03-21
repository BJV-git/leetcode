# first add the numbers till that number and rest to next.
# now for every next iteration add and subtract elements instead of repeated calculations

def pivotIndex(nums):
    len_nums=len(nums)
    sum1 = sum(nums[:0])
    sum2 = sum(nums[1:])

    if len_nums < 3:
        return -1
    # elif sum(nums[1:])==0:
    #     return 0
    else:
        for i in range(0,len_nums):
            if sum1==sum2:
                return i
            if i != len_nums-1:
                sum1+=nums[i]
                sum2-=nums[i+1]
    return -1

print(pivotIndex([-1,-1,-1,-1,-1,-1]))
