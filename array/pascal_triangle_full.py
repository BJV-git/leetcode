# logic : have the window of two
# observation: from diagram we see that its a sum of previous line's  same and previous index.
# can use the fibonacci
def generate(index):
    output = []
    def getRow( rowIndex):
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
    for i in range(index):
        output.append(getRow(i))
    print(output)

generate(0)
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