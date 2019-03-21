# normal way: is ot count the possible neighbours and add up

def island_per(grid):
    count=0
    r,c = len(grid), len(grid[0])

    for i in range(r):
        for j in range(c):
            if grid[i][j]==1:
                # a=[[k,l] for k,l in ([i-1,j], [i+1,j], [i,j-1], [i,j+1]) if 0<=k<r and 0<=l<c]
                # print(a)
                possible = [grid[z[0]][z[1]]==0 for z in [[k,l] for k,l in ([i-1,j], [i+1,j], [i,j-1], [i,j+1]) if 0<=k<r and 0<=l<c]]
                edges = sum(possible)
                spcl = (((i==0)+(i==r-1) + (j==0)+(j==c-1)))

                count+= spcl+edges
                # print(i, j, possible, spcl,count, '\n')

    return count

print(island_per([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))