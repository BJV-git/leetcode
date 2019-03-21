# logic : to take all things as arrays. Now comparing them as slices and returning the status
# next: take an array of size col-1 and then edit in such a way that we expect the next correct one

#edge cases: single row and single column

def isToeplitzMatrix(matrix):
    rows,cols = len(matrix), len(matrix[0])
    if rows==0 and cols==0:
        return False
    elif rows==1 or cols==1:
        return True
    else:
        expect=matrix[0][:-1]
        i=1
        while i<rows:
            print(expect)
            if matrix[i][1:] == expect:
                del expect[-1]
                expect.insert(0, matrix[i][0])
                i += 1
                continue

            else:
                return False

        return True

m=[
  [1]
]
# print(m[1][1:])

print(isToeplitzMatrix(m))
# a=[1,2,3,4]
# print(a[:-1])