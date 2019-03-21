# find the degree keys and return the min range
def findShortestSubArray(nums):
    len_nums=len(nums)

    final={}
    for i in nums:
        final[i] = final.get(i,0)+1
    degree = max(final.values())
    values = [i for i,j in final.items() if j == degree]
    return min(   [  len_nums -nums[::-1].index(i)   - nums.index(i) for i in values])

print(findShortestSubArray([1,2]))