# logic: how we do is the same way to do it, setting limits and then for each change changing the limits and moving on


def generateMatrix(n):
    matrix = [[0 for i in range(n)] for i in range(n)]
    val = 1
    top_limit, bottom_limit, right_limit, left_limit = 0,n,n,0
    loop = n*2 - 1

    while loop >= 0:

        # move right
        for i in range(left_limit, right_limit):
            # print(left_limit)
            # print(right_limit)
            matrix[top_limit][i] = val
            val+=1
        # print(matrix)
        loop -= 1


        top_limit +=1

        # move down
        for i in range(top_limit, bottom_limit):
            matrix[i][right_limit-1]=val
            val+=1
        loop -= 1

        # print(matrix)

        right_limit -= 1


        # move left
        for i in range(right_limit-1, left_limit-1, -1):
            matrix[bottom_limit-1][i] = val
            val+=1
        loop -= 1
        # print(matrix)


        bottom_limit -=1


        #move up
        for i in range(bottom_limit-1, top_limit-1, -1):
            matrix[i][left_limit]=val
            val+=1
        loop -= 1
        # print(matrix)

        left_limit +=1

    return matrix

a = generateMatrix(3)
print(a)