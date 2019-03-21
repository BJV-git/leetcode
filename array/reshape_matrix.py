def matrixReshape( nums, r, c):
    rows,cols= len(nums), len(nums[0])

    if rows*cols != r*c:
        return nums
    else:
        new_matrix = [[None] * c for _ in range(r)]
        nums=[i for sub in nums for i in sub]
        if r==1 and c==rows*cols:
            return [].append(nums)
        len_nums = len(nums)
        count=0
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = nums[count]
                count+=1
        return new_matrix
print(matrixReshape([[1,2],[3,4]],2,4))


#
# a=[]
# b=[1,2,3]
# a.append(b)
# print(a)