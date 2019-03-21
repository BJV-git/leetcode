# logic : take the indices of the elements that are greater than the r, which has the potential of breaking the sub-array , not the less one
# after individual count, find the slices and return the sum

# pattern: coming from last, if its a number > lmits then count set to 0, if in range from that point to limit = add up
# if less than range then just carry on

def numSubarrayBoundedMax(A, L, R):
    len_A = len(A)
    summ=0
    i=len_A-1
    limit = len_A
    temp=0
    while i >=0:
        # print(i)
        if A[i] > R:
            limit = i
            # summ+=temp
            temp=0
            # print("here summ is ", summ)
        if A[i] <=R and A[i] >=L:
            # print("A[i]", A[i])
            temp= limit - i
            # print("temp value updated", temp)
        # else:
        #     temp+=temp
        summ += temp
        # print("sum at {0} is {1}".format(i, summ))
        i-=1
    # print("out temp",  temp)

    # summ+=temp
    return summ

print(numSubarrayBoundedMax([4], 2,3))