# logic: just keep all the logics possible
# also one way of solving the sum is that forming lower triangle with the upper triangle

def numMagicSquaresInside(grid):
    rows, cols = len(grid), len(grid[0])
    if rows <3 or cols < 3:
        return 0
    else:
        check=[]
        summ=0
        for i in range(rows-2):
            for j in range(cols-2):
                total = sum(grid[i][j:j+3])

                if sum(grid[i][j:j+3]) + sum(grid[i+1][j:j+3]) + sum(grid[i+2][j:j+3]) == 45 and not any( z>9 for z in  grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]  ):

                    if grid[i+1][j+2] == total -grid[i+1][j] - grid[i+1][j+1]:
                        if (grid[i+2][j+1] == total - grid[i][j+1] - grid[i+1][j+1]):
                            if (grid[i+2][j+2] == total -grid[i+2][j] - grid[i+2][j+1]):
                                if grid[i][j] + grid[i+1][j+1]+ grid[i+2][j+2] == grid[i][j+2] + grid[i+1][j+1]+ grid[i+2][j]:
                                    summ+=1
        return summ

print(numMagicSquaresInside([[1,8,6],[10,5,0],[4,2,9]]))

