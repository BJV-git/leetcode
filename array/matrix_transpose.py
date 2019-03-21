# logic: just while forming new matrix retrieve from previous but i and j interchanged

def transpose(A):
    B=[]
    rows, cols = len(A), len(A[0])
    for i in range(cols):
        temp=[]
        for j in range(rows):
            temp.append(A[j][i])
        B.append(temp)
    return B

print(transpose([[1]]))
