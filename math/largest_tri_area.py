# lets find the wideest in terms of x and y
# now,

# basically we need to find the outer most 3 points covering all the other points
# we can find the 4 using x and y simply

# the basic assumption made is not true that the outers make the largest area and now we go by brute force method for now
import math
import sys
import itertools
def largest_tri_area(points):
    maxi=0
    for iter in itertools.combinations(points,3): # which takes all the 3 combinations of the points
        maxi = max(maxi, abs((iter[0][0]*(iter[1][1]-iter[2][1]) + iter[1][0]*(iter[2][1]-iter[0][1]) + iter[2][0]*(iter[0][1]-iter[1][1]))*0.5))
    return maxi

        # left=[sys.maxsize, 0]
        # right=[-sys.maxsize, 0]
        # top=[0,-sys.maxsize]
        # bottom=[0,sys.maxsize]
        #
        # if len(points)==3:
        #     left, top, right = points[0], points[1], points[2]
        #     return abs(float((left[0] - top[0])*(right[1]- top[1]) - (right[0] - top[0])*(left[1] - top[1]))/2)
        # if len(points)==4:
        #     points.sort(key=lambda x: [x[0],-x[1]])
        #     left, right, top, bottom = points[0], points[3], points[1], points[2]
        #     area1 = abs(float((left[0] - top[0]) * (right[1] - top[1]) - (right[0] - top[0]) * (left[1] - top[1])) / 2)
        #     area2 = abs(float((left[0] - bottom[0]) * (right[1] - bottom[1]) - (right[0] - bottom[0]) * (left[1] - bottom[1])) / 2)
        #
        #     left,right, top, bottom = top, bottom, left, right
        #     area3 = abs(float((left[0] - top[0]) * (right[1] - top[1]) - (right[0] - top[0]) * (left[1] - top[1])) / 2)
        #     area4 = abs(float((left[0] - bottom[0]) * (right[1] - bottom[1]) - (right[0] - bottom[0]) * (left[1] - bottom[1])) / 2)
        #
        #     # print(area1, area2)
        #     # print(left, right, top, bottom)
        #
        #     return max(max(area1, area2), max(area3, area4))
        #
        # for p in points:
        #     print(p)
        #     if p[0] < left[0]and p not in [ right, top, bottom]:
        #         left=p
        #     if p[0] > right[0]and p not in [left, top, bottom]:
        #         right=p
        #     if p[1] < bottom[1] and p not in [top,left,right]:
        #         bottom=p
        #     if p[1] > top[1] and p not in [bottom,left,right]:
        #         top=p
        #
        #     print([left, right, top, bottom])
        #
        #     print('')
        # for p in points:
        #     print(p)
        #     if p[0] < left[0]and p not in [ right, top, bottom]:
        #         left=p
        #     if p[0] > right[0]and p not in [left, top, bottom]:
        #         right=p
        #     if p[1] < bottom[1] and p not in [top,left,right]:
        #         bottom=p
        #     if p[1] > top[1] and p not in [bottom,left,right]:
        #         top=p
        # print([left, right, top, bottom])
        #
        # area1 = abs(float((left[0] - top[0]) * (right[1] - top[1]) - (right[0] - top[0]) * (left[1] - top[1])) / 2)
        # area2 = abs(float((left[0] - bottom[0]) * (right[1] - bottom[1]) - (right[0] - bottom[0]) * (left[1] - bottom[1])) / 2)
        #
        # left, right, top, bottom = top, bottom, left, right
        # area3 = abs(float((left[0] - top[0]) * (right[1] - top[1]) - (right[0] - top[0]) * (left[1] - top[1])) / 2)
        # area4 = abs(float((left[0] - bottom[0]) * (right[1] - bottom[1]) - (right[0] - bottom[0]) * (left[1] - bottom[1])) / 2)
        #
        # # print(area1, area2)
        # # print(left, right, top, bottom)
        #
        # return max(max(area1, area2), max(area3, area4))



print(largest_tri_area([[9,0],[1,10],[7,6],[3,9]]))