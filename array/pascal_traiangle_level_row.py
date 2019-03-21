# logic : have the window of two
# observation: from diagram we see that its a sum of previous line's  same and previous index.
# can use the fibonacci

def getRow( rowIndex):

    # def find_value(level, index):
    #
    #     if index == level or index ==0:
    #         return 1
    #
    #     else:
    #         return (find_value(level-1, index) + find_value(level-1, index-1))
    # if rowIndex == 0:
    #     return [1]
    # elif rowIndex ==1:
    #     return [1,1]
    # else:
    #     res=[1]
    #     res.extend([find_value(rowIndex,i) for i in range(1,rowIndex)])
    #     res.append(1)
    #
    # return res
    arr=[]
    if rowIndex == 0:
        arr= [1]
    elif rowIndex ==1:
        arr= [1,1]
    else:
        arr=[1,1]
        for i in range(rowIndex-1):
            temp= [ (arr[i] + arr[i+1]) for i in range(len(arr)-1)]
            arr = [1] + temp +[1]
    return arr



print(getRow(3))


#     pt = []
#     pt.append(1)
#     for i in range(1,rowIndex):
#         pt.append(find_value(rowIndex, i))
#     pt.append(1)
#
#     print(pt)
#
# getRow(3)
# l=1
# i=0
# print((l,i)in [(0,0),(1,0),(1,1)])