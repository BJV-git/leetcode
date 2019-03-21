# learned logic: first keep track of the left side product until that number and in reverse do to the right
def productExceptSelf(nums):
    if nums:
        len_nums = len(nums)
        output=[]
        if len_nums <= 2:
            return nums
        else:
            p=1
            for i in range(len_nums):
                output.append(p)
                p=p*nums[i]
            p=1
            for i in range(len_nums-1,-1,-1):
                output[i]=output[i]*p
                p=p*nums[i]

            return output

print(productExceptSelf([1,2,3,4]))