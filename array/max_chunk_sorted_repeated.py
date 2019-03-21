# logic : so let it be multiple numbers. assuming that its has been sorted, now if we compare the sorted to the initial we see that loops are
# formed. so no of loops == no of chunks

# worked except for [1,1,0,0,1]
# now the additional thing to add is that need to verify that if the temp set has all from start to farthest

def maxChunksToSorted(arr):
    max_chunks = 0
    len_arr = len(arr)
    temp=set() # for visited indices
    temp.add(0)
    i=0
    if len_arr == 1: # checking if len ==1
        return 1
    elif sorted(arr) == arr: # if already in sorted then no need of counting (will consume extra, so can remove)
        return len_arr
    # elif sorted(arr) == arr[::-1]:
    #     return 1

    else:
        arr=[[arr[i],i] for i in range(len_arr)]
        arr.sort(key=lambda x: x[0])
        # print("arr_sorted", arr)
        start=0
        farthest = 0
        i=0
        next_index=0
        while i < len_arr:
            # print(temp)
            next_index = arr[i][1]
            farthest = max(farthest, next_index) # is to store the last index of the loop and then store to move next

            if next_index==i or next_index in temp:
                if len(set(range(start,farthest+1)) -temp) == 0:
                    max_chunks+=1
                    i = farthest+1
                    start=i
                    temp=set()
                    temp.add(i)
                    farthest=0
                    continue
                else:
                    i = list(set(range(start,farthest+1)) - temp)[0]
                    temp.add(i)
                    continue
            i=next_index
            temp.add(next_index)

    return max_chunks

# print(maxChunksToSorted([1,1,0,0,1]))
print('max',maxChunksToSorted([5,1,1,8,1,6,5,9,7,8]))

    #
    #         if arr[i] ==i and flag==0:
    #             limit+=1
    #             max_chunks+=1
    #             i+=1
    #             continue
    #         if arr[i]> i and flag==0:
    #             maxi = arr[i]
    #             flag=1
    #             # continue
    #         if maxi == len_arr-1 and flag==1:
    #             max_chunks += 1
    #             break
    #         if arr[i]==limit:
    #             max_chunks+=1
    #             flag=0
    #             limit=maxi+1
    #             maxi=0
    #         i+=1
    #
    # return max_chunks




# print(maxChunksToSorted([0,4,5,2,1,3]))
# a=[3,3,1,3,4,3]
# #
# #
# # # a=[5,4,3,2,1]
# a=[[a[i],i] for i in range(len(a))]
# print(a)
# a.sort(key=lambda x: x[0])
# print(a)

