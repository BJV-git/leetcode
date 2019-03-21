#logic: first trying to get the details of the columns top be nullified and also deleting the rows at same time.
# later using the indicators to nullify the columns

def setZeroes( matrix):
    m,n = len(matrix), len(matrix[0])
    col_zeros = [0 for i in range(n)]

    for i in range(m):

        if 0 in matrix[i]:
            temp = [1 if matrix[i][j] == 0 else 0 for j in range(n)]
            col_zeros = [1 if j > 0 else 0 for j in [x+y for x, y in zip (col_zeros , temp)]]
            matrix[i] = [0 for i in range(n)]


    for i in range(m):
        temp = matrix[i]
        matrix[i] = [0 if col_zeros[i] == 1 else temp[i] for i in range(n)]

    print(matrix)
    # return matrix

#
# continue
# else:
# temp = matrix[i]
# matrix[i] = [0 if col_zeros[i] == 1 else temp[i] for i in range(n)]



setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])