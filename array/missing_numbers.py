def findDisappearedNumbers( nums):
    len_nums = len(nums)
    print (set(range(1, len_nums + 1)) - set(nums))
findDisappearedNumbers([4,3,2,7,8,2,3,1])