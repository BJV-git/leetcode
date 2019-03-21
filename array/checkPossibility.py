# logic: let us say that we have a reserve of left = count to allow the no of modifications
# except the first rest has same logic
# [3,4,2,3] learned logic is to have a limit
# imagining the graph as a continuous increasing or constant graph mathematically

# logic: if increasing check the three every iteration are in increasing order or not
def checkPossibility(nums):
    len_nums=len(nums)
    limit=0
    left=1

    if len_nums<3:
        return True
    elif len_nums==3:
        if nums[2] < nums[1] and nums[1] < nums[0]:
            return False
        else:
            return True
    else:

        if nums[0] > nums[1]:
            nums[0]=nums[1]
            left-=1
        if nums[len_nums-1] < nums[len_nums-2]:
            nums[len_nums-1] = nums[len_nums-2]
            left-=1
        for i in range(len_nums-2):
            if left < 0:
                return False
            elif nums[i] <= nums[i+2]:
                if (nums[i] > nums[i+1] or nums[i+1] > nums[i+2]):
                    nums[i+1]=nums[i]
                    left-=1
            else:
                print("yes")
                nums[i+2] = nums[i+1]
                print(nums)
                left-=1
            if left < 0:
                return False

        return True

print(checkPossibility([1,3,2,2,2]))