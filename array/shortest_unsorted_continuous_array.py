def findUnsortedSubarray(nums):
    len_nums=len(nums)
    num1=sorted(nums)
    start=0
    end=0
    for i in range(len_nums):
        if nums[i]!=num1[i]:
            start=i
            break
    for i in range(len_nums-1, -1,-1):
        if (nums[i]!= num1[i]):
            end=i
            break
    if start==end==0:
        return 0
    return(end-start+1)
print(findUnsortedSubarray([1,2,3,4]))




    # if len_nums <=1:
    #     return nums
    # else:
    #     count=0
    #     start=0
    #     min_pos=0
    #     end=len_nums-1
    #     for i in range(len_nums-1):
    #         if nums[min_pos]> nums[i] and( count==0 or count==1):
    #             start=0
    #             count+=1
    #         elif nums[i] > nums[i+1]:
    #             if count==0:
    #                 start=i
    #                 count+=1
    #                 continue
    #             end=i
    #     if start==0:
    #         return 0
    #
    # print("start", start)
    # print("end", end+1)

findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])