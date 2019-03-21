# logic: irrespective of how the cubes are placed, we know that
# count + max of each (on one side) and + max of each on other side

def proj_area(grid):
    arr_len = len(grid[0])

    count = 0
    each_max=0

    max_arr = [0]*arr_len

    for i in grid:
        maxi=0
        for j in range(arr_len):
            if i[j] !=0:
                count+=1
            max_arr[j] = max(i[j], max_arr[j])
            maxi = max(maxi, i[j] )
        each_max+=maxi
    return each_max + count + sum(max_arr)
