# return the peak fo the index

def peak(A):
    flag = 0
    la=len(A)

    for i in range(la-1):
        if A[i] > A[i+1]:
            return i
    return la-1