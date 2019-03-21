

def valid_mount(A):
    lena = len(A)
    if lena <3 :
        return False

    flag = 0 # means increasing

    for i in range(lena-1):
        if A[i] == A[i+1]:
            return False
        if flag ==0 and A[i] > A[i+1]:
            if i==0:
                return False
            flag =1
            continue

        if flag == 1 and A[i] < A[i+1]:
            return False

    return True and flag==1