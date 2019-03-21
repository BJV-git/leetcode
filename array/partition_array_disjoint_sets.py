# logic: additional to checking all the elements again and again for all the elements from right
# can sort and compare the two for which the right most are equal

# not work as

# the first element is max, we try to find the min if anything less than the max and return the distance
# if min == max return 1

# worked fine but if happen to have a number max than first element and then a min later to the pos failed  [32,57,24,19,0,24,49,67,87,87]
# if chosen that maxi gets updated and find the min doesn't work either as in [5,0,3,8,6] even 6 < 8 but 6 > rest 3 in beginning

# so after getting the pos, once we check the maxi in the slice if happen to find any of the maxi >,
# then we come from last and return when encountered the 1st min


def partitionDisjoint(A):
    mini = maxi = A[0]
    l = len(A)
    pos = 0
    for i in range(1, l):
        if A[i] < maxi:
            mini = A[i]
            pos = i
    if mini == maxi:
        return 1
    else:
        maxi = max(A[:pos+1])
        for i in range(l-1,-1,-1):
            if A[i] < maxi:
                return i+1
        # return pos + 1
    # print("pos", pos)
print(partitionDisjoint([32,57,24,19,0,24,49,67,87,87]))
# [5,0,3,8,6]