# so the logic is to go through each element and see where the no decreasing are indices and return the length
# but we need to compare with the other same indices too

# so better to use a dic, to get hold of the indices and current one, as anyways we only need the latest one previosu are unnecessary

def minDel(A):
    A=[i.strip() for i in A]
    l = len(A[0])
    d={i:'' for i in range(l)}


    indices=set()

    for i in A:
        for j in range(l):
            if d[j] is not None:
                if d[j] <= i[j]:
                    d[j] =  i[j]
                else:
                    d[j]=None
        print(d)
    return sum(j==None for i,j in d.items())

print(minDel(["rrjk","furt","guzm"]))