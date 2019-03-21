def flipAndInvertImage(A):
    rows = cols = len(A)
    for i in range(rows):
        A[i].reverse()
        A[i] = [1 if j==0 else 0 for j in A[i]]
    return A

print(flipAndInvertImage([[1]]))