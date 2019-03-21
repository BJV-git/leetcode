# so irrespective of array we can make all of them equal in n number of moves
# we can eliminate the sort and take the max

# logic: sort and add to first n-1 numbers
def minMoves(nums):
    if not nums: return 0
    mini = min(nums)
    moves = 0
    for i in nums:
        moves += i - mini
    return moves



    # len_nums = len(nums)
    # moves = 0
    # maxi = max(nums)

    # while True:
    #     if len(set(nums))==1:
    #         break
    #
    #     i=0
    #     flag = 0
    #     moves+=1
    #     while i < len_nums:
    #         if nums[i] == maxi and flag==0:
    #             flag = 1
    #             i+=1
    #             continue # dont increment
    #
    #         nums[i]+=1
    #         maxi = max(maxi,nums[i])
    #         i+=1
    # print(nums)
    # return moves

print(minMoves([1,10, 10, 12, 100]))
