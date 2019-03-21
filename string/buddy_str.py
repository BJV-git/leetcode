# logic: go through the both strings
# when encountered a diff means we need to find the ones in opposite things at same time
# if extra reject

def buddy_strs(A,B):
    flag=0
    a=None
    b=None

    alen=len(A)
    blen = len(B)

    if not A or not B or alen != blen:
        return False

    if A==B and len(A) != len(set(A)):
        return True


    for i in range(alen):



        if A[i]!=B[i]:
            if flag==0:
                a=B[i]
                b=A[i]
                flag=1
            elif flag ==1: # means already the first mismatch is found
                if A[i] !=a or B[i] != b:
                    return False
                else:
                    flag =2
            else:
                return False
    if flag==0:
        return False
    return True

print(buddy_strs('ab','ab'))