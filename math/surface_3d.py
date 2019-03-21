# logic: 3 things

# 1. no of items as base * 2 the top also
# 2.

# from previous projection, we can add max and the min

# got it: when inside misses, we get extra counts

# logic 1: while looking in each direction we need to make sure if any is lesser, so that extra spaces are created.
# and that's the only thing we need to be added


# Aaaah!!! - just imagine like a snake crawling throiugh the cubes and how it would od to cover all teh surface area
# the way I thought is a wrap whirling through the entire structure

import sys
def surfc_3(grid):
    surface=0
    r ,c = len(grid), len(grid[0])

    for row in range(r):
        for col in range(c):

            edges = ((row==0) + (row==r-1) + (col==0)+(col==c-1))
            surface+= grid[row][col]*edges

            if row!=r-1:
                surface += abs(grid[row][col] - grid[row+1][col])
            if col!=c-1:
                surface += abs(grid[row][col] - grid[row][col+1])
            if grid[row][col] > 0:
                surface+=2
    return surface
print()




    # arr_len = len(grid[0])
    #
    # count = 0
    # each_max = 0
    # each_min = 0
    #
    # max_arr = [0] * arr_len
    # min_arr = [sys.maxsize] * arr_len
    #
    # for i in grid:
    #     maxi = 0
    #     mini=sys.maxsize
    #     for j in range(arr_len):
    #         if i[j] != 0:
    #             count += 1
    #         max_arr[j] = max(i[j], max_arr[j])
    #         min_arr[j] = min(i[j], min_arr[j])
    #         maxi = max(maxi, i[j])
    #         mini = min(mini, i[j])
    #
    #     each_max += maxi
    #     each_min += mini

    # return each_max + (2*count) + sum(max_arr) + sum(min_arr) + each_min

# print(surfc_3([[3,3,3],[3,4,5],[5,0,4]]))