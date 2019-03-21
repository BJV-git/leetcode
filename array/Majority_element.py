# logic use dict to calculate the frequency and result it
def majorityElement( nums):
    len_nums = len(nums)
    result=[]
    d={}
    if nums:
        for i in nums:
            if (i) not in d.keys():
                d[(i)] = 1
            else:
                d[(i)] = d[(i)] + 1

        result = [i for i,j in d.items() if j > len_nums//3]
    print(result)
    return result


majorityElement([1,2])