#logic: If can see the pattern that the if no are arranged then need to just add the even indexed ones
def arrayPairSum( nums):
    nums.sort()
    return sum(nums[0::2])
# a=[1,2,3,4,5,-1]
# a.sort()
# print(sum(a[0::2]))