# logic: keep track of the largest found continuous one and move on as if like finding the max in an array
def findLengthOfLCIS(nums):
    max_length=0

    temp_len=1
    if nums:
        len_nums = len(nums)
        for i in range(len_nums-1):
            if nums[i] < nums[i+1]:
                temp_len+=1
            else:
                max_length = max(max_length, temp_len)
                temp_len=1
        return max(max_length, temp_len)
    return 0
print(findLengthOfLCIS([1,-1]))