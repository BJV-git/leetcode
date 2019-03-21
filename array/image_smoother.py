def imageSmoother(M):
    rows, cols = len(M), len(M[0])
    new_matrix= [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            # print("row and column", i, j)

            neighbours = [(i+1,j+1),(i,j+1),(i+1,j),(i-1,j-1),(i-1,j),(i,j-1),(i+1,j-1),(i-1,j+1), (i,j)]
            possible_neighbours = [(i,j) for i,j in neighbours if 0<=i<rows and 0<=j<cols]
            score = sum(M[i][j] for i,j in possible_neighbours)
            new_matrix[i][j] = int(score/len(possible_neighbours))

    print(new_matrix)

imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])