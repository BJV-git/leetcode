# again can use the dicts to keep track of the count of numbers, and the the difference based on the number we have encountered
# so that can get in O(n) time, i.e. just in two passes
# one more is that we can use try in order to escape checking the dict if key is available

# can also use the set to have same time complexity as dict ??? true ????

def array_pair_sum(arr, sum):
    count={}
    diff={}
    pairs=0

    for i in arr:
        count[i] = count.get(i,0)+1
        diff[i] = sum - i

    for i in arr:
        try:
            if count and count[diff[i]]>0 and count[i]> 0:
        # if diff[i] in count and count[diff[i]]>0 and count[i]> 0:

                count[i]-=1
                count[diff[i]]-=1
                pairs+=1
        except:
            pass
            #
            # print("i", i)
            # print("diff", diff)
            # print("count", count)
            # print("")

    return pairs


print(array_pair_sum([1,2,1,3],3))
# print(array_pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))