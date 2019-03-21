
# learned: when eidting the array, we need to use updatd values always
# learned: its just keeping the zeroes last we need to put the value last, returninf the len

def remove_elem(nums, val):
    zeros = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[zeros] = nums[zeros], nums[i]
            zeros += 1

    return zeros

    i=0
    j=0

    while i < len(nums):
        if nums[i]!=val:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j+=1
        else:
            i+=1
    return j

    # i = 0
    # while i < len(nums):
    #     if nums[i] == val:
    #         nums.remove(nums[i])
    #         i -= 1
    #     i += 1
    # return len(nums)

    # i = 0  # learned no in this way as we might end up running out as we are removing numbers
    # l = len(nums)
    # while i < l:
    #     if nums[i] == val:
    #         nums.remove(nums[i])
    #         i -= 1
    #
    #     i += 1
    # return len(nums)

print(remove_elem([0,1,2,2,3,0,4,2],
2))