# logic: once from left to right, and again reversed.
# will consider the min of the both appended. and consider max if none is encountered from start or min if put maax value to it.

def maxDistToClosest(seats):
    len_seats = len(seats)
    compare =[]
    pos = -40000

    for i in range(len_seats):
        if seats[i] == 1:
            pos=i
            compare.append([0])
        else:
            compare.append([i-pos])
    pos = 40000
    for i in range(len_seats-1, -1, -1):
        if seats[i] == 1:
            pos=i
            compare[i].extend([0])
        else:
            compare[i].extend([pos-i])
    print(compare)
    return max([min(i,j) for i,j in compare])
print(maxDistToClosest([0,0,1,0,1,0,0,1,0,0]))