# logic : coming from reverse, if can see how many increasing orders are there -> solution, counting by seeing how many i > i+1
# while testing test cases max = len and min =1. so solved
# if diff is 1 only

# in the question he has given the index as len and are permutation. so we can treat index as sorted list, no need of sorting again and
# jump to that specific index and start from its next and increase its max chunks

#  logic: count+1 for all the ones in place and res count to 1 each in between, so u cut it. so no of cuts +1

# sensible logic: when u hit a number max than its index keep in max and search for its index and repeat process. when met set max = null or zero
# but if met the max in middle can jump to last and add chunk to 1
# use flag, logic is that if we see num > index means wec expext a loop from that index to numbers index to chunk it and shuffle
# to make sure that rest isnt disturbed so until no inplace chunk addition

def maxChunksToSorted(arr):
    max_chunks = 0
    maxi=0
    flag=0
    len_arr = len(arr)
    i=0
    if len_arr == 1:
        return 1
    elif sorted(arr) == arr:
        return len_arr
    elif arr[len_arr-1]==0:
        return 1
    else:
        while i < len_arr:
            maxi = max(maxi, arr[i])
            if arr[i] ==i and flag==0:
                max_chunks+=1
                i+=1
                continue
            if arr[i]> i and flag==0:
                flag=1
                # continue
            if maxi == len_arr-1 and flag==1:
                max_chunks += 1
                break
            if i==maxi:
                max_chunks+=1
                flag=0
                maxi=0
            i+=1

    return max_chunks

print(maxChunksToSorted([0,4,5,2,1,3]))

        #     if arr[i]==i:
        #         print("i",i)
        #         print("arr i", arr[i])
        #         cuts+=1
        #     i+=1
        # return cuts+1


        # while i >= 0:
        #     next = arr[i]
        #     if next < i:
        #         i = next
        #         continue
        #     elif next >=i:
        #         max_chunks += 1
        #         i-=1
        #     # if i <= next:
        #     #     i -= 1
        #     #
        #     # else:
        #     #     i = next - 1
        #     #
        #     # if i == 0 and arr[0] == 0:
        #     #     max_chunks += 1
        #     #     break
        #
        # return max_chunks

