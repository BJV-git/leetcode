#logic: first to find the index of the greatest one and then to exchange it with its successor and then reverse the stuff
def nextPermutation( nums):
    if nums:
        len_nums = len(nums)
        start=len_nums-1
        end=0
        once=0

        for i in range(start,-1, -1):
            if nums[i-1]< nums[i]:
                end=i
                break
        if end == 0:
            nums.reverse()
            return nums
        else:
            limit = ((start+end)//2 + ((start+end)%2))-1
            for i in range(start,end-1, -1):
                if nums[i] > nums[end-1]:
                    nums[end - 1], nums[i] = nums[i], nums[end - 1]
                    break
            for i in range(start,limit ,-1):
                nums[i], nums[start+end-i]= nums[start+end-i],nums[i]
            return nums

print(nextPermutation([5,4,7,5,3,2]))