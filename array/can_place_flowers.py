# see the both ends, also measuring the length gives a big advantage. can search for 3 and if found means can fit in the numbers
def canPlaceFlowers(flowerbed, n):
    len_bed=len(flowerbed)
    possible_no_max = len_bed//2 + len_bed%2
    current=0
    search=0
    if n==0:
        return True
    elif n>possible_no_max or sum(i==1 for i in flowerbed)==possible_no_max:
        return False
    elif len_bed ==1:
        if flowerbed[0]==1:
            return False
        else:
            return True
    else:
        if flowerbed[0] + flowerbed[1] == 0:
            current += 1
            flowerbed[0] = 1
        if flowerbed[len_bed - 1] + flowerbed[len_bed - 2] == 0:
            current += 1
            flowerbed[len_bed - 1] = 1
        print(flowerbed)
        print(current)
        for i in range(1,len_bed-1):
            if flowerbed[i]==0:
                search+=1
                # print("search", search)
                if search==3:
                    current+=1
                    search=1
            else:
                search=0
            if current>=n:
                return True

        # print(current)
        # print(flowerbed)
        if current==n:
            return True
        else:
            return False
#
# if flowerbed[0]+flowerbed[1] ==0 or flowerbed[len_bed-1]+flowerbed[len_bed-2]==0:
#         return True
#     else:
#         search = 0
#         for i in range(1,len_bed-1):
#             if flowerbed[i]==0:
#                 search+=1
#             elif search ==3:
#                 return True
#             else:
#                 search=0
print(canPlaceFlowers([1,0,0,0,1],1))