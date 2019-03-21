# logic:

def isMonotonic(A):

    flagg = 0
    flag_set = 0
    prev = A[0]

    for i in A:
        curr = i
        diff = prev-curr
        if flag_set ==0:
            if diff < 0:
                flagg -= 1
                flag_set = 1
            if diff > 0:
                flagg+=1
                flag_set = 1

        if (flagg ==1 and diff < 0) or (flagg==-1 and diff >0):
            return False
        prev = curr

    return True
    #     if flag_dec <2:
    #         if prev > curr:
    #             flag_inc = 2
    #         if prev < curr and flag_inc ==2:
    #             return False
    #     if flag_inc < 2:
    #         if prev < curr:
    #             flag_inc = 2
    #         if prev > curr and flag_dec ==2:
    #             return False
    #     prev = curr
    # return True

print(isMonotonic([-1000,1,1,-1]))