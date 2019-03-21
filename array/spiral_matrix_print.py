# logic: how we do is the same way to do it, setting limits and then for each change changing the limits and moving on


def spiralOrder(matrix):
    output=[]
    if matrix:
        rows=len(matrix)
        cols = len(matrix[0])
        top_limit, bottom_limit, right_limit, left_limit = 0,rows,cols,0
        if rows < cols or (rows==cols):
            loop = 2*rows-1
        else:
            loop = 2*cols
        output=[]
        print(rows,cols)
        while loop >= 0:

            # move right
            for i in range(left_limit, right_limit):
                # print(left_limit)
                # print(right_limit)
                output.append(matrix[top_limit][i])
            print(output)
            loop -= 1
            if loop==0:
                break

            top_limit +=1

            # move down
            for i in range(top_limit, bottom_limit):
                output.append(matrix[i][right_limit-1])
            loop -= 1
            if loop==0:
                break

            print(output)

            right_limit -= 1


            # move left
            for i in range(right_limit-1, left_limit-1, -1):
                output.append(matrix[bottom_limit-1][i])
            loop -= 1
            if loop==0:
                break
            print(output)


            bottom_limit -=1

            #move up
            for i in range(bottom_limit-1, top_limit-1, -1):
                output.append(matrix[i][left_limit])
            loop -= 1
            if loop==0:
                break
            print(output)

            left_limit +=1

    return output

a = spiralOrder([
 [ 1,6,5,4,8,9,10]

])

# print(a)
