# rotating the matrix by 90 degree
# logic: if looked at the patterns, we can do by rotating squares and iterating thru each square
def rotate(matrix):
    if matrix and len(matrix)>1:
        dim=len(matrix)
        # print(dim)
        loops = dim//2
        # print(loops)
        for i in range(loops):
            start_i= start_j = i # starting at the top corner left of the square
            print("i",i)
            for j in range(i,dim-(i+1)):
                print("j",j)
                top_i, top_j = i,j
                right_i, right_j= top_j, dim-1-top_i
                bottom_i, bottom_j= right_j, dim-1-right_i
                left_i, left_j= bottom_j, dim-1-bottom_i
                matrix[right_i][right_j], matrix[bottom_i][bottom_j], matrix[left_i][left_j], matrix[top_i][top_j] =matrix[top_i][top_j], matrix[right_i][right_j], matrix[bottom_i][bottom_j], matrix[left_i][left_j]
    return matrix

print(rotate([1]))

# for i in range(0,5):
#     print(i)