# logic: sort and start from last to half of the element as it is enough to make sure rest are small, if found return
# better is that second best should be such that less than half
def dominantIndex(nums):
    len_nums=len(nums)

    if len_nums==1:
        return 0
    else:
        maxi_index = nums.index(max(nums))

        nums.sort()
        max_num=nums[-1]
        sec_max=nums[-2]
        if max_num >= 2*sec_max:
            return maxi_index
        else:
            return -1

print(dominantIndex([3, 4]))